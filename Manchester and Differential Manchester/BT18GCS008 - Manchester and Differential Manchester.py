import numpy as np
import matplotlib.pyplot as plt

'''
Program by: Yash Jain, BT18GCS008
This program takes a bit sequence as an input and outputs 2 graphs.
The graphs show Manchester and Differential Manchester Encoding repectively.
This code considers 0 as a low to high signal and 1 as a high to low signal.
For Differential Manchester Encoding, the signal inverses on input 0.
'''

num_bits=int(input("Number of bits:"))
y=[]
manchester=[]
diff_manchester=[]
bits=[]
j=0

print("Enter the bits:")
for i in range(num_bits):
    y.extend((i, i+0.5, i+0.5, i+1))

for i in range(num_bits):
    num=int(input())
    bits.append(num)
    if num==1:
        manchester.extend((1, 1, -1, -1))
        if len(diff_manchester)==0:
            diff_manchester.extend((1, 1, -1, -1))
        else:
            x=[diff_manchester[-4],diff_manchester[-1]]
            diff_manchester.extend((x[1], x[1], x[0], x[0]))
    elif num==0:
        manchester.extend((-1, -1, 1, 1))

        if len(diff_manchester)==0:
            diff_manchester.extend((-1, -1, 1, 1))
        else:
            x=[diff_manchester[-4],diff_manchester[-1]]
            diff_manchester.extend((x[0], x[0], x[1], x[1]))

fig, (axs1, axs2) = plt.subplots(1, 2)
axs1.plot(y, manchester)
axs1.set_title("Manchester Encoding")
axs1.set(xlabel="Time", ylabel="Amplitude")
axs2.plot(y, diff_manchester)
axs2.set_title("Different Manchester Encoding")
axs2.set(xlabel="Time", ylabel="Amplitude")
plt.show()