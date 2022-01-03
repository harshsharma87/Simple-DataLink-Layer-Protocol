# Simple-DataLink-Layer-Protocol

Using socket programming to set up a simple data link layer protocol between a computer and a server.

Project Goal:

   1. To generate a random payload message of 1024 bits and form test packages. Each frame contains a header of 01111110 with a frame counter of 1 byte. 
   2. CRC checking is done by using the divisor 𝑥^4 + 𝑥^3 + 1 i.e. 11001.
   3. The server will bounce back the packets at a packet error rate of 20% randomly and perform CRC at the client side and check for any errors.
   4. We have to use ARQ (Automatic Repeat Request) to ignore incorrect packets by comparing CRC of sent and received message and resend until the CRC matches.
   
• Plot the transmission end to end latency and the package drop rate.

• To read a jpeg image in binary format using computer or telephone and pack the bit stream into I frames with a size of 1024 bit. The received image should be an image without distortion.
