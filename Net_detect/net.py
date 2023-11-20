import tkinter as tk
import psutil

root = tk.Tk()
root.geometry('300x150')
root.iconbitmap(r'C:\Users\ichen\PycharmProjects\python_study\images\speed2.ico')
root.title('网速监测工具')
root.config(background='#cde8f3')
tk.Label(
    root,
    text='网络速度',
    background='#cde8f3',
    font=('宋体', 25, 'bold'),
    fg='#4198b9'
).pack(pady=15)

speed_val = tk.StringVar(value='')
tk.Label(
    root,
    textvariable=speed_val,
    background='#cde8f3',
    font=('Arial', 20, 'bold'),
    fg='#6bb3c0'
).pack()


def speed_test(pre_data):
    cur_data = psutil.net_io_counters().bytes_recv
    data = (cur_data - pre_data) / 1024
    speed_val.set(f'{data:.1f}K/s'if data < 1024 else f'{data/1024:.1f}M/s')
    root.after(1000, speed_test, cur_data)


speed_test(psutil.net_io_counters().bytes_recv)

root.mainloop()
