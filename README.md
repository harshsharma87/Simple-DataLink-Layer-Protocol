# Simple-DataLink-Layer-Protocol

Using socket programming to set up a simple data link layer protocol between a computer and a server.

**Data link layer:**

The Data link layer is the second layer in Open System Interconnection (OSI) model of computer networking that transfers data between different network nodes in a WAN or nodes on same LAN.

• It defines the format of the packets exchanged between the nodes at the ends of the link and taken by these nodes when sending and receiving packets.
• The packets exchanged are called frames and that each Data Link-layer frame typically encapsulates one network-layer datagram.

**Demo Link**
https://youtu.be/Hnsu2JvqtPk

**Project Goal:**

   1. To generate a random payload message of 1024 bits and form test packages. Each frame contains a header of 01111110 with a frame counter of 1 byte. 
   2. CRC checking is done by using the divisor 𝑥^4 + 𝑥^3 + 1 i.e. 11001.
   3. The server will bounce back the packets at a packet error rate of 20% randomly and perform CRC at the client side and check for any errors.
   4. We have to use ARQ (Automatic Repeat Request) to ignore incorrect packets by comparing CRC of sent and received message and resend until the CRC matches.
   
• Plot the transmission end to end latency and the package drop rate.

• To read a jpeg image in binary format using computer or telephone and pack the bit stream into I frames with a size of 1024 bit. The received image should be an image without distortion.

**FRAME CONFIGURATION**
Header - 01111110 ;
Divisor - 11001 ;
Payload -  1024 bits ;
Frame Counter - 1 Byte

**LEARNING FROM THE PROJECT**

1. Learn about socket programming and how to do programming using server and client.
2. How to use CRC to transmit a message and how it affects the information carried by the message.
3. How to convert a JPEG image into binary format.
4. From a Network point of view, understood how end to end latency works and how it affects the time taken for packet transmission.

