'''
Program by: Yash Jain, BT18GCS008.
This program offers 2 choices: Vertical and Longitudinal Redundancy Check.
The user is expected to input Signals for the Receiver and Sender both.
For VRC, Enter an 8-bit Binary string for Receiver and the 8-bit Binary string with the parity bit for Receiver.
For LRC, Enter the Binary String with spaces in between every 8-bits for the Receiver 
and the Binary String with the parity bits for the Sender.
'''
bit={True:['0','1'],False:['1','0']}
def LRC_Sender(row_wise):
    for i in range(len(row_wise)):
        if even:
            if row_wise[i].count('1')%2==0:
                row_wise[i]+=bit[even][0]
            else:
                row_wise[i]+=bit[even][1]
    row_wise.append('')
    for i in range(len(row_wise[0])):
        temp=''
        for j in range(len(row_wise)-1):
            temp+=row_wise[j][i]
        if even:
            if temp.count('1')%2==0:
                row_wise[-1]+=bit[even][0]
            else:
                row_wise[-1]+=bit[even][1]
    print(row_wise)
def LRC_Receiver(row_wise):
    checkbit=['','']
    for i in range(len(row_wise)):
        if even:
            if row_wise[i].count('1')%2==0:
                checkbit[0]+=bit[even][0]
            else:
                checkbit[0]+=bit[even][1]
    for i in range(len(row_wise[0])):
        temp=''
        for j in range(len(row_wise)):
            temp+=row_wise[j][i]
        if even:
            # print(temp)
            # print(temp.count('1'))
            if temp.count('1')%2==0:
                checkbit[1]+=bit[even][0]
            else:
                checkbit[1]+=bit[even][1]
    print(checkbit)
    if '1' in checkbit[0] or '1' in checkbit[1]:
        print('There is/are %d error/s in the Received Signal'%(checkbit[0].count('1')+checkbit[1].count('1')))
    else:
        print('There are no errors')
def VRC_Sender(binary):
    if even:
        if binary.count('1')%2==0:
            binary+=bit[even][0]
        else:
            binary+=bit[even][1]
    print(binary)
def VRC_Receiver(binary):
    checkbit=bit[even][0] if binary.count('1')%2==0 else bit[even][1]
    if checkbit == '1':
        print("There is an error in the Received Signal")
    else:
        print("There is no error")
choice='y'
while choice=='y':
    print("Choose:\n1)Vertical Redundancy Check\n2)Longitudinal Redundancy Check")
    choice=int(input())
    even=True if input("Choose:\n1)Even Parity\n2)Odd Parity\n")=='1' else False
    if choice==1:
        binary=input("Enter a binary string for the Sender:\n")
        VRC_Sender(binary)
        binary=input("Enter a binary string for the Receiver:\n")
        VRC_Receiver(binary)
    elif choice==2:
        binary=input("Enter a binary string for the Sender:\n")
        LRC_Sender(binary.split())
        binary=input("Enter a binary string for the Receiver:\n")
        LRC_Receiver(binary.split())
    choice=input("Do you want to continue?(Y/n)\n")
    choice.lower()