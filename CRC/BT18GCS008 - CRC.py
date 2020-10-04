'''
Program by: Yash Jain, BT18GCS008.
This program implements CRC. 
The user is required to enter the Frame and Generator for the Sender.
The user is required to enter the Received Coded Data for the Receiver.
The Output shows Coded Data from the Sender side and checks for errors both through CRC and Manual check.
'''
def CRC(data):
    temp=data[:crc_bits+1]
    pos=crc_bits+1
    for i in range(len(input_data)-crc_bits):
        if temp[0]=='1':
            res=str(bin(int(temp,2)^int(divisor,2)))[2:].zfill(3)
        else:
            res=temp[1:]
        if i==len(input_data)-crc_bits-1:
            break
        temp=res+data[pos]
        pos+=1
    return temp

input_data=input("Enter Frame: ")
divisor = input("Enter Generator: ")
crc_bits=len(divisor)-1
for i in range(crc_bits):
    input_data+="0"
pos=crc_bits+1
crc=0
temp=input_data[0:crc_bits+1]
res=0
temp=CRC(input_data)
crc=temp[1:]
coded_data=input_data[:-3]+crc
print("The Coded Data: ",coded_data)
pos=crc_bits+1
temp=coded_data[0:crc_bits+1]
receiver_data=input("Enter Data for the Receiver: ")
temp=CRC(receiver_data)
if temp[1:]=='000':
    if input_data[:-3]==receiver_data[:-3]:
        print("No error even after manual check")
        print("Extracted Data: ", receiver_data[:-3])
    else:
        print("No error through CRC Check but error through manual check.\nDiscarding data.")
else:
    print("Error in data through CRC check.\nDiscarding data")
