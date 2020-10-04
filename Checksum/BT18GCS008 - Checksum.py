'''
Program by: Yash Jain, BT18GCS008.
This program implements checksum for 4-bit and 16-bit input.
The user is asked to choose between 4-bit and 16-bit.
The program takes input signal with space between each value.
The program outputs Sum, Wrapped Sum, Checksum, Transmitted Signal for Sender side.
The program outputs Sum, Wrapped Sum, Checksum, Presense of error for Receiver side.
This is a continuous program and will continue till user inputs y or Y.
'''
def sender4bit(input4bit):
    list4bit=[int(i) for i in input4bit.split()]
    sum4bit=sum(list4bit)
    print("Sum: ", sum4bit)
    while sum4bit>15:
        temp=str(bin(sum4bit))[2:]
        sum4bit=int(temp[-4:], 2) + int(temp[:-4], 2)
    print("Wrapped Sum: ",sum4bit)
    checksum=int('0b1111', 2)
    checksum=int(str(bin(checksum)), 2) - int(str(bin(sum4bit))[2:], 2)
    print("Checksum: ",checksum)
    return str(checksum)
def sender16bit(input16bit):
    list16bit=input16bit.split()
    if len(list16bit)%2==0:
        ascii16bit=[format(ord(list16bit[i]), 'x')+format(ord(list16bit[i+1]), 'x') for i in range(0,len(list16bit),2)]
    else:
        ascii16bit=[format(ord(list16bit[i]), 'x')+format(ord(list16bit[i+1]), 'x') for i in range(0,len(list16bit)-2,2)]
        ascii16bit.append(format(ord(list16bit[-1]), 'x'))
    sum16bit=int('0', 16)
    for i in ascii16bit:
        sum16bit+= int(i, 16)
    sum16bit=str(hex(sum16bit))[2:]
    print("Sum: ", sum16bit)
    while len(sum16bit)>4:
        sum16bit=str(hex(int(sum16bit[-4:],16)+int(sum16bit[:-4],16)))[2:]
    print("Wrapped Sum: ",sum16bit)
    checksum=str(hex(int('FFFF',16) - int(str(sum16bit), 16)))[2:]#.format('04x')
    if checksum=='0':
        print("Checksum: 0000")
        return '0000'
    # print(checksum)
    checksum=format(int(checksum, 16),'04x')
    
    checksum=chr(int(checksum[:2], 16))+' '+str(chr(int(checksum[2:], 16)))
    print("Checksum: ",checksum)
    return checksum
while True:
    print("Choose:\n1)4-bit Input\n2)16-bit Input")
    choice=int(input())
    if choice==1:
        input4bit=input("Enter numbers from 0-15 with spaces in between.\n")
        checksum1=sender4bit(input4bit)
        print("Transmitted Signal: ", input4bit+' '+checksum1)
        receive4bit=input("Enter the received signal with the checksum.\n")
        checksum2=sender4bit(receive4bit)
        if checksum2=='0':
            print("No error")
        else:
            print("Error")
    elif choice==2:
        input16bit=input("Enter Letters with spaces in between.\n")
        checksum1=sender16bit(input16bit)
        print("Transmitted Signal: ", input16bit+' '+checksum1)
        receive16bit=input("Enter Letters with spaces in between.\n")
        checksum2=sender16bit(receive16bit)
        if checksum2=='0000':
            print("No error")
        else:
            print("Error")
    choice=input("Do you want to continue? (Y/n)\n")
    if choice=='n':
        break
    elif choice.lower()!="y":
        print("Incorrect Input")
        break