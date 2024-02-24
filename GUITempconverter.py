import tkinter as tk
from tkinter import ttk

class TemperatureConverter:
    @staticmethod
    def fahrenheit_to_celsius(f):
        celsius = (f - 32) * 5/9
        
        return f"Here is the celsius value: {celsius:.2f}"

    @staticmethod
    def celsius_to_fahrenheit(c):
        fahrenheit = c * 9/5 + 32
        return f"Here is the fahrenheit value: {fahrenheit:.2f}"
    
class ConverterFrame(ttk.Frame):
    
    def __init__(self, container, unitfrom, converter):
        super().__init__(container)

        self.unitfrom = unitfrom
        self.converter = converter

        
        self.temp_label = ttk.Label(self, text=self.unitfrom)
        self.temp_label.grid(column=0, row=0, sticky='w', padx=5, pady=0)

        self.inputvalue = tk.StringVar()
        self.temp_entry = ttk.Entry(self, textvariable=self.inputvalue)
        self.temp_entry.grid(column=1, row=0, sticky = 'w', padx=5, pady=0)
        self.temp_entry.focus()

        self.con_button = ttk.Button(self, text='Convert')  
        self.con_button.grid(column=2,row=0, sticky='w', padx=5, pady=0)
        self.con_button.configure(command=self.calculate)

        self.result_label = ttk.Label(self)
        self.result_label.grid(columnspan=3, row=1, padx=5,pady=0)
                
        self.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")

        
    def calculate(self):
        temp = float(self.inputvalue.get())
        result = self.converter(temp)
        self.result_label.config(text=result)

    def reset(self):
        self.temp_entry.delete(0, "end")
        self.result_label.text = ''

class Controlframe(ttk.LabelFrame):

    def __init__(self, container):
        super().__init__(container)
        self['text'] = 'Options'
        self.selected_value = tk.IntVar()
        ttk.Radiobutton(self, text='f to c',
                        value=0, variable=self.selected_value, 
                        command=self.change_frame).grid(column=0, row=0, padx=5, pady=5)
        ttk.Radiobutton(self, text='c to f',
                        value=1, variable=self.selected_value,
                        command=self.change_frame).grid(column=1, row=0, padx=5, pady=5)
        
        self.grid(column=0, row=1, padx=5, pady=5, sticky=tk.EW)

        self.frames = {}
    
        self.frames[0] = ConverterFrame(
            container,
            'Fahrenheit',
            TemperatureConverter.fahrenheit_to_celsius)
        self.frames[1] = ConverterFrame(
            container,
            'Celsius',
            TemperatureConverter.celsius_to_fahrenheit)
        
        self.change_frame()

    def change_frame(self):
        frame = self.frames[self.selected_value.get()]
        print(frame)
        frame.reset()
        frame.tkraise()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Temperature Converter')
        self.geometry('300x120')
        self.resizable(False, False)
        
if __name__ == "__main__":
    app = App()
    Controlframe(app)
    app.mainloop()
