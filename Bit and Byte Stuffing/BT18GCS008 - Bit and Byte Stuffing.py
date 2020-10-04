
'''
Program by: Yash Jain, BT18GCS008
This program offers 2 choices: Byte Stuffing and Bit Stuffing.
Enter a string and the outputs after Stuffing and Destuffing will be displayed.
The program is in a continuous loop.
'''

choice='y'
while choice.lower()=='y':
    print("Choose:")
    print("1) Byte Stuffing")
    print("2) Bit Stuffing")
    choice=input()
    if choice=='1':
        x=input("Enter the String: ")
        flag=input("Enter Flag")
        escape_char=input("Enter Escape Character")
        
        print("After Byte Stuffing: ", x)
        x=x[1: len(x)-1].replace(escape_char+flag, flag)
        print("After Byte Destuffing: ", x)
    elif choice=='2':
        x=input("Enter the String: ")
        print("The Flag will be 01111110")
        x=''.join(format(ord(i), '08b') for i in x)
        print("Before Bit Stuffing:\t ", x)
        x="01111110"+x.replace("11111", "111110")+"01111110"
        print("After Bit Stuffing:\t ", x)
        x=x[8:-8].replace("111110", "11111")
        print("After Bit Destuffing:\t ", x)
        stringlist=[x[i:i+8] for i in range(0, len(x), 8)]
        string=''.join([chr(int(i, 2)) for i in stringlist])
        print("Confirming: ", string)
    else:
        print("Wrong Input, Choose again")
    choice=input("Do you want to continue?(Y/n)")
