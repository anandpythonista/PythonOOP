from tkinter import *
from tkinter import filedialog

def fileopen():
    filepath = filedialog.askopenfilename()
    file = open(filepath, 'r')
    print(file.read())

app = Tk()
app.title("File Dialog App")
button = Button(text='file open', command=fileopen)
button.pack()
app.mainloop()
