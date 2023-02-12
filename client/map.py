from doctest import master
import matplotlib.pyplot as plt
from tkinter import *
import numpy as np
import pandas as pd
import time


t = 0

master = Tk()


w = Canvas(master, width=750, height=540)


w.create_rectangle(30, 10, 120, 80,
                   outline="#fb0")
w.create_rectangle(150, 10, 240, 80,
                   outline="#f50")
w.create_rectangle(270, 10, 360, 80,
                   outline="#05f")
w.pack()


df = pd.read_csv('slider.log', delimiter=' ', header=None)
# print(df)
x = [10*i for i in df.index]
# print(df[0])
y_1 = df[0]
y_2 = df[1]
y_3 = df[2]

# with open('slider.log', 'r') as f:
#     time.sleep(10)
#     lines = f.readlines()
#     last_line = lines[-1].split()
#     # DATA = {"avg_v_effective": last_line[0], "avg_eff_acc": last_line[1], "avg_pwr_rtio": last_line[2]}
#     global x
#     x.append(t)
#     global y_1
#     y_1.append(last_line[0])
#     global y_2
#     y_2.append(last_line[1])
#     global y_3
#     y_3.append(last_line[2])
#     # print(last_line)


# using subplot function and creating plot one
plt.subplot(1, 3, 1)  # row 1, column 3, count 1
plt.plot(x, y_1, 'r', linewidth=5, linestyle=':')
plt.title('FIRST PLOT')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# using subplot function and creating plot two
# row 1, column 3, count 2
plt.subplot(1, 3, 2)

# g is for green color
plt.plot(x, y_2, 'g', linewidth=5)
plt.title('SECOND PLOT')
plt.xlabel('x-axis')
plt.ylabel('y-axis')


plt.subplot(1, 3, 3)

# g is for green color
plt.plot(x, y_2, 'g', linewidth=5)
plt.title('THIRD PLOT')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# space between the plots


# show plot
plt.show()

master.mainloop()
