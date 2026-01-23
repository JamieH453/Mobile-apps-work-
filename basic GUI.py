def button_clicked():
    print("Button was clicked!")

import tkinter as tk

window = tk.Tk()

window.title("My First App")

window.geometry("400x300")

window.configure(bg="lightblue")    

label = tk.Label(window, text="Hello")

button = tk.Button(window, text="Click Me")
command=button_clicked

button.pack()

entry = tk.Entry(window)
entry.pack()

window.mainloop()
