import tkinter as tk
# from tkinter import *
# from tkinter import ttk
# import requests
# import time

## init vars to be global
dt = 100  # 0.1 sec
count = 0
acc = 0
brk = 0
v = 0
v_eff_sum = 0
eff_acc = 0
pwr_rtio = 0

# root window
root = tk.Tk()
root.geometry('720x540')
root.resizable(False, False)
root.title('Slider Demo')
root.configure(bg='green')


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


# slider current value

current_variable1 = tk.DoubleVar()
current_variable2 = tk.DoubleVar()
current_variable3 = tk.DoubleVar()
current_variable4 = tk.DoubleVar()


def slider_changed(event):
    var1 = vertical1.get()
    var2 = vertical2.get()
    print(var1, var2)
    # DATA = {"acc":var1, "brake":var2}
    # time.sleep(10)
    # r = requests.post(url="http://localhost:5000/json", json=DATA)
    # print(r.text)


vertical1 = tk.Scale(root, from_=0.00, to=2.00, resolution=0.005, troughcolor='#73B5FA', orient=tk.HORIZONTAL,
                     label="Acceration", width=30, sliderlength=30, length=500, variable=current_variable1)  # , command=slider_changed)
vertical1.pack()

vertical2 = tk.Scale(root, from_=0.00, to=2.00, resolution=0.005, troughcolor='#FF0000', orient=tk.HORIZONTAL,
                     label="Brake", width=30, sliderlength=30, length=500, variable=current_variable2)  # , command=slider_changed)
vertical2.pack()

vertical3 = tk.Scale(root, from_=0.00, to=10.00, resolution=0.01, troughcolor='#00FF00', orient=tk.HORIZONTAL,
                     label="Postition", width=30, sliderlength=30, length=500, variable=current_variable3)  # , command=slider_changed)
vertical3.pack()

vertical4 = tk.Scale(root, from_=0.00, to=10.00, resolution=0.01, troughcolor='#0000FF', orient=tk.HORIZONTAL,
                     label="Obstacle", width=30, sliderlength=30, length=500, variable=current_variable4)  # , command=slider_changed)
vertical4.pack()


def task():
    global count
    global acc
    global brk
    acc += vertical1.get()
    brk += vertical2.get()
    count += 1
    # print(count, acc, brk)

    m = 1000  # Mass of vehicle in Kg

    global v
    v = v + acc*dt/1000
    pa = m*acc*(v)
    v_effective = v-brk*dt/1000
    p_effective = m*brk*(v_effective)
    # print(pa,p_effective)
    if pa != 0:
        power_ratio = (p_effective/pa)*100

    global v_eff_sum
    v_eff_sum += v_effective
    global eff_acc
    eff_acc += (acc-brk)
    global pwr_rtio
    if pa != 0:
        pwr_rtio += power_ratio

    if count >= 10000/dt:
        with open('slider.log', 'a') as f:
            print(format(v_eff_sum/count, ".2f"), format(eff_acc/count,".2f"), format(pwr_rtio/count,".2f"), file=f, sep=' ')
            # print(v_eff_sum/count, (eff_acc/count), pwr_rtio/count)format(acc/count, ".2f"), format(brk/count, ".2f"),
        acc = 0
        brk = 0
        count = 0
        v_eff_sum = 0
        eff_acc = 0
        pwr_rtio = 0

    root.after(dt, task)  # reschedule event in 2 seconds


root.after(dt, task)

root.mainloop()
