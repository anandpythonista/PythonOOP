import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class textFrame(tk.Frame):
    def __init__(self, container, textbox):
        super().__init__(container, borderwidth=2)
        self.grid(row=0, column=0, sticky=tk.NS)
        self['relief'] = 'raised'
        self.open_button = ttk.Button(self, text='open file', command=self.open_file)
        self.open_button.grid(column=0, row=0, sticky=tk.EW)
        self.save_button = ttk.Button(self, text='save file', command=self.save_file)
        self.save_button.grid(column=0, row=1, sticky=tk.EW)
        self.textbox = textbox

    def open_file(self):
        filetypes = (('text file', '*.txt'), ('All files', '*.*'))
        filepath = filedialog.askopenfilename(filetypes=filetypes)
        file = open(filepath, 'r')
        self.textbox.insert('1.0', file.read())

    def save_file(self):
        filetypes = (('text file', '*.txt'), ('All files', '*.*'))
        content = self.textbox.get('1.0', 'end')
        filepath = filedialog.asksaveasfilename(filetypes=filetypes)
        file = open(filepath, 'w')
        file.write(content)

class textBox(tk.Text):
    def __init__(self, container):
        super().__init__(container, height=300, width=400)
        self.grid(column=1, row=0)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x400')
        self.resizable(False, False)
        self.title('Text Editor App')
        self.rowconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)

        self.textpad = textBox(self)
        self.leftframe = textFrame(self, self.textpad)
        

        self.mainloop()

if __name__ == "__main__":
    myapp = App()

