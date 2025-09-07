
import tkinter as tk
from tkinter import messagebox
import math

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("450x600")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=20)

def click_button(value):
    entry.insert(tk.END, value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        expression = expression.replace('√', 'math.sqrt')
        expression = expression.replace('^', '**')
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed.")
        entry.delete(0, tk.END)
    except:
        messagebox.showerror("Error", "Invalid Input")
        entry.delete(0, tk.END)

buttons = [
    ['7', '8', '9', '/', '(', ')'],
    ['4', '5', '6', '*', '√', '^'],
    ['1', '2', '3', '-', 'C', 'pi'],
    ['0', '.', '=', '+', 'sin', 'cos'],
    ['tan', 'log', 'ln', 'exp', '%', 'abs']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for button in row:
        if button == "=":
            b = tk.Button(frame, text=button, font=("Arial", 16), command=calculate)
        elif button == "C":
            b = tk.Button(frame, text=button, font=("Arial", 16), bg="red", fg="white", command=clear_entry)
        elif button == "pi":
            b = tk.Button(frame, text=button, font=("Arial", 16), command=lambda: click_button(str(math.pi)))
        elif button in ['sin','cos','tan','log','ln','exp','abs','√','^']:
            b = tk.Button(frame, text=button, font=("Arial", 16), command=lambda x=button: click_button(x+'(' if x not in ['√','^'] else x))
        else:
            b = tk.Button(frame, text=button, font=("Arial", 16), command=lambda x=button: click_button(x))
        b.pack(side="left", expand=True, fill="both")

root.mainloop()
