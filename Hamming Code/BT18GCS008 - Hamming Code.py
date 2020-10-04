'''
Program by: Yash Jain, BT18GCS008.
This program implements Hamming Code.
For Sender Side, the user is asked to input a data code and choose between Even or Odd Parity.
For Receiver Side, the user is asked to input the Received Code Word and choose between Even or Odd Parity.
The Output shows the position of the error in case it exists.
'''
import math
dataword=input("Enter Data Word:\n")
m=len(dataword)
even=True if input("Choose:\n1)Even Parity\n2)Odd Parity\n")=='1' else False
parity={True:['0','1'],False:['1','0']}
r=0
binarySeq=[]
codeword=''
parityBits={}
while True:
    if 2**r>=m+r+1:
        break
    else:
        r+=1
paritypos=[2**i -1 for i in range(r)]
count=0
for i in range(m+r):
    if i in paritypos:
        bit=' '
    else:
        bit=dataword[count]
        count+=1
    codeword+=bit
for i in range(2**r):
    temp=str(bin(i))[2:]
    while len(temp)<r:
        temp='0'+temp
    binarySeq.append(temp)
for i in range(r):
    temp=[]
    for j in range(len(binarySeq)):
        if binarySeq[j][::-1][i]=='1':
            temp.append(int(binarySeq[j], 2)-1)
    parityBits[2**i-1]=temp
while True:
    temp=''
    pos=codeword.find(' ')
    if pos==-1:
        break
    for i in parityBits[pos]:
        if i>m+r-1:
            continue
        temp+=codeword[i]
    bit=parity[even][0] if temp.count('1')%2==0 else parity[even][1]
    codeword=codeword[:pos]+bit+codeword[pos+1:]
print("After Applying Hamming Code:",codeword)
receiverCode=input("Enter Received Side Code:\n")
even=True if input("Choose:\n1)Even Parity\n2)Odd Parity\n")=='1' else False
checkBit={i: '' for i in parityBits.keys()}
for i in parityBits:
    temp=''
    for j in parityBits[i]:
        if j>m+r-1:
            continue
        temp+=receiverCode[j]
    checkBit[i]=parity[even][0] if temp.count('1')%2==0 else parity[even][1]
errorLoc=0
error=False
for i in checkBit.items():
    if i[1] =='1':
        error=True
        errorLoc+=i[0]+1
if error:
    print("Error exists at position ", errorLoc)
else:
    print("No error")