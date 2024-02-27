import tkinter as tk
from tkinter import ttk
import time

def click():
    count = 0
    download = 100
    while count < download:
        time.sleep(0.05)
        count += 1
        bar['value'] = count
        percent = count/download * 100
        message.set('download is in progress' + str(int(percent)) +'%')
        root.update_idletasks()

root = tk.Tk()
root.title('Download page')
root.geometry('300x150')

bar = ttk.Progressbar(root)
bar.pack(pady=20)

message = tk.StringVar()

label = ttk.Label(root, textvariable=message)
label.pack(pady=10)

button = ttk.Button(root, text='download', command=click)
button.pack(pady=10)

root.mainloop()