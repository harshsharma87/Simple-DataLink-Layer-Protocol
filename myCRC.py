#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 16:07:28 2020

@author: iamharsh
"""

import socket
import numpy as np
import time
from matplotlib.pyplot import figure, plot, grid
import matplotlib.pyplot as plt
import os

latency = []

def bt2int(bt):
    w = 2 ** np.array(range(8))[::-1]
    return np.dot(bt, w)

def msg2bt(msg):
    bt = []
    for i in range(len(msg)):
        for b in msg[i]:
            bt.append(int(b))
    return bt

def appendBitToResult(resultArray, bit):
    resultArray.append(bit)

def xor(bit_seq, divisor):
    xorOutput = '' 
    resultArray = []
    for i in range(1, len(divisor)):
        if bit_seq[i] != divisor[i]:
            appendBitToResult(resultArray, '1')  #function call to append bit to resultArray.
            continue   #goes to next iteration.
        
        appendBitToResult(resultArray, '0')      #function call to append bit to resultArray.
    
    return xorOutput.join(map(str, resultArray)) #converts resultArray to string & returns it.

#CRC code is generated by dividing new binary seq by the divisor & eliminating initial-zero's from remainder.
def getCRC(divident, divisor): 
    divident = convertListToString(divident)
    divisor_length = len(divisor)
    
    #To begin, reduce the divident to the length of divisor.
    temp_rem = divident[0 : divisor_length] 
    
    for bitsToBePick in range(divisor_length , len(divident)):
        if temp_rem[0] == '1':  
            temp_rem = xor(divisor, temp_rem) + str(divident[bitsToBePick]) 
            continue
        
        temp_rem = xor('0'*bitsToBePick, temp_rem) + str(divident[bitsToBePick]) 

    if temp_rem[0] == '1': #if final execution array starts w/ 1, XOR the array & return it.
        crc = list(xor(divisor, temp_rem))
        
#if final execution array doesn't starts w/ 1, first remove starting 0's, XOR the array & return it       
    else:
        crc = list(xor('0'*bitsToBePick, temp_rem))
    
    return convertStringListToIntList(crc)
    
def convertListToString(test_list):         # e.g. [0, 1, 1, 1, 1, 1, 1, 0] -> 01111110
    test_list = [int(i) for i in test_list]   
    s= [str(i) for i in test_list]
    return "".join(s)

def convertStringListToIntList(test_list):  # e.g. 01111110 -> [0, 1, 1, 1, 1, 1, 1, 0]
    test_list = [int(i) for i in test_list] 
    return test_list

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('23.235.207.63', 9993) #change ports from 9990-9999
print('PACKET TRANSMISSION STARTED')
with open('umdlogo.jpg','rb') as f:
#with open('umdCECS.png','rb') as f:
#with open('umdearborn.jpg','rb') as f:
    buff = f.read()
msg = ['{:08b}' .format(b) for b in buff]
bt = msg2bt(msg)
N, cnt, rdata = 1024, 0, bytes([])
errorCount=0
Nf = int(np.ceil(len(bt)/N))
Nout = 1
sock.settimeout(0.1)
successCount=0
totalHits=0
totalpackets=0
while True:
    pcktCntr=0
    totalpackets+=1
    myframe = list([0, 1, 1, 1, 1, 1, 1, 0])
    cntArr = [int(b) for b in '{:08b}'.format(cnt)]
    myframe += cntArr
    txData = bt[1024 * cnt:1024 * (cnt + 1)]
    myframe += txData
    mycrc1 = getCRC(myframe, '11001')
    myframe+=mycrc1
    myframe+=[0, 0, 0, 0]
    myframe=np.array(myframe).reshape(int(len(myframe)/8), 8)
    myPacket=[bt2int(b) for b in myframe]
    ts1 = time.time()
    
    while True:
        pcktCntr+=1
        totalHits+=1
        try:
            sent = sock.sendto(bytes(myPacket), server_address)
            data, server = sock.recvfrom(2048)
            ts2 = time.time()
        except socket.timeout:
            Nout += 1
            
        rev = ['{:08b}'.format(b) for b in data][:-1]
        rev = msg2bt(rev)
        mycrc2 = getCRC(rev, '11001')
        if(mycrc1 != mycrc2) : #comparing crc of sent and received message
            errorCount+=1
        else:
            break  
            
    latency.append((ts2 - ts1) * 1e3)
    print("Packet",cnt, "succesfully transmitted in",pcktCntr, "attempts")  
    trimData=data[2:len(data)-1] #trims incoming data 
    rdata+=trimData
    
    if cnt == Nf:
        print('Done')
        break

    cnt+=1
    

with open('recievedlogo.jpg', 'wb') as f:
    f.write(rdata)
    
print('Error count during data transmission : ', errorCount)
print('Total packets sent to server: ', totalpackets)
print('Total hits(error+success) to server : ', totalHits)
print('FILE HAS BEEN RECEIVED.')
fig = figure(1, figsize = (8, 6))
plot(latency)
plt.xlabel('No. of packets -->>')
plt.ylabel('Time -->>')
plt.title('End to End Latency')
grid(True)
fig.savefig('Latency', dpi = 300)
os.system('open latency.png')
os.system('open recievedlogo.jpg')
