def greet():
    name=name_entry.get()
    greeting_label.config(text=f"Hello, {name}!")       

def create_greeting_label():
    global greeting_label
    greeting_label=tk.Label(window, text="", bg="lightblue", font=("Arial", 16))
    greeting_label.pack(pady=10)

def clear_greeting():
    global greeting_clear_button
    greeting_label.config(text="")

def clear_name():
    name_entry.delete(0, tk.END)
    
import tkinter as tk
from unicodedata import name
window=tk.Tk()
window.title("Greeting app")
window.geometry("1400x1500")
window.config(bg="lightblue")

instruction_label=tk.Label(window, text="Enter your name:", bg="white", font=("Arial", 14, "bold"))
instruction_label.pack(pady=10)

name_entry=tk.Entry(window, font=("Arial", 14))
name_entry.pack(pady=10)

greeting_clear_button=tk.Button(window, text="Clear Greeting", command=clear_greeting, font=("Arial", 12))
greeting_clear_button.pack(pady=5)

name_clear_button=tk.Button(window, text="Clear Name", command=clear_name, font=("Arial", 12))
name_clear_button.pack(pady=5)


greet_button=tk.Button(window, text="Greet", command=greet, font=("Arial", 14))
greet_button.pack(pady=10)

greeting_label=tk.Label(window, text="", bg="lightblue", font=("Arial", 16))
greeting_label.pack(pady=10)    
create_greeting_label()
 
window.mainloop()
