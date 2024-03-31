
import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN
from calculator import Calculator

calc = Calculator()
window = tk.Tk()
window.title('Calculator')
frame = tk.Frame(master=window, padx=10)
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=4, ipady=2, pady=2 ,padx=10)


def myClick(number):    
    entry.insert(tk.END, number)

def equal():
    try:
        result = calc.evaluate_expression(entry.get())
        print(result)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")


def clear():
	entry.delete(0, tk.END)


button_1 = tk.Button(master=frame, text='1', padx=15,
					pady=5, width=3, command=lambda: myClick(1))
button_1.grid(row=1, column=1, pady=2)
button_2 = tk.Button(master=frame, text='2', padx=15,
					pady=5, width=3, command=lambda: myClick(2))
button_2.grid(row=1, column=2, pady=2)
button_3 = tk.Button(master=frame, text='3', padx=15,
					pady=5, width=3, command=lambda: myClick(3))
button_3.grid(row=1, column=3, pady=2)
button_4 = tk.Button(master=frame, text='4', padx=15,
					pady=5, width=3, command=lambda: myClick(4))
button_4.grid(row=2, column=1, pady=2)
button_5 = tk.Button(master=frame, text='5', padx=15,
					pady=5, width=3, command=lambda: myClick(5))
button_5.grid(row=2, column=2, pady=2)
button_6 = tk.Button(master=frame, text='6', padx=15,
					pady=5, width=3, command=lambda: myClick(6))
button_6.grid(row=2, column=3, pady=2)
button_7 = tk.Button(master=frame, text='7', padx=15,
					pady=5, width=3, command=lambda: myClick(7))
button_7.grid(row=3, column=1, pady=2)
button_8 = tk.Button(master=frame, text='8', padx=15,
					pady=5, width=3, command=lambda: myClick(8))
button_8.grid(row=3, column=2, pady=2)
button_9 = tk.Button(master=frame, text='9', padx=15,
					pady=5, width=3, command=lambda: myClick(9))
button_9.grid(row=3, column=3, pady=2)
button_0 = tk.Button(master=frame, text='0', padx=15,
					pady=5, width=3, command=lambda: myClick(0))
button_0.grid(row=4, column=2, pady=2)

button_add = tk.Button(master=frame, text="+", padx=15,
					pady=5, width=3, command=lambda: myClick('+'))
button_add.grid(row=1, column=0, pady=2)

button_subtract = tk.Button(
	master=frame, text="-", padx=15, pady=5, width=3, command=lambda: myClick('-'))
button_subtract.grid(row=2, column=0, pady=2)

button_multiply = tk.Button(
	master=frame, text="*", padx=15, pady=5, width=3, command=lambda: myClick('*'))
button_multiply.grid(row=3, column=0, pady=2)

button_div = tk.Button(master=frame, text="/", padx=15,
					pady=5, width=3, command=lambda: myClick('/'))
button_div.grid(row=4, column=0, pady=2)

button_clear = tk.Button(master=frame, text="clear",
						padx=15, pady=5, width=12, command=clear)
button_clear.grid(row=6, column=0, columnspan=2, pady=2)


button_equal = tk.Button(master=frame, text="=", padx=15,
						pady=5, width=9, command= equal )
button_equal.grid(row=6, column=2, columnspan=3, pady=2)
