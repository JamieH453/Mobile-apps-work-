def add():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 + num2
    result_label.config(text="Result: " + str(result))
def subtract():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 - num2
    result_label.config(text="Result: " + str(result))

def multiply():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 * num2
    result_label.config(text="Result: " + str(result))
    
def divide():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    if num2 != 0:
        result = num1 / num2
        result_label.config(text="Result: " + str(result))
    else:
        result_label.config(text="Error: Division by zero")

def clear_answer():
    result_label.config(text="Result: ")  
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)

from cProfile import label
import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("1000x1000")
window.config(bg="lightgrey")

grid0 = tk.Label(window, text="Number 1:", font=("Arial", 14), bg="lightgrey")
grid0.pack(pady=10)


entry1 = tk.Entry(window, font=("Arial", 14))
entry1.pack(pady=10)

grid1 = tk.Label(window, text="Number 2:", font=("Arial", 14), bg="lightgrey")
grid1.pack(pady=10)

entry2 = tk.Entry(window, font=("Arial", 14))
entry2.pack(pady=10)

add_button = tk.Button(window, text="Add", command=add, font=("Arial", 14))
add_button.pack(pady=5)

subtract_button = tk.Button(window, text="Subtract", command=subtract, font=("Arial", 14))
subtract_button.pack(pady=5)

multiply_button = tk.Button(window, text="Multiply", command=multiply, font=("Arial", 14))
multiply_button.pack(pady=5)

divide_button = tk.Button(window, text="Divide", command=divide, font=("Arial", 14))
divide_button.pack(pady=5)

clear_button = tk.Button(window, text="Clear", command=clear_answer, font=("Arial", 14))
clear_button.pack(pady=5)

result_label = tk.Label(window, text="Result: ", font=("Arial", 16), bg="lightgrey")
result_label.pack(pady=20)

window.mainloop()