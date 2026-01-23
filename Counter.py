
import tkinter as tk 

def increase():
    global count
    count += 1
    counter_label.config(text=str(count))

def decrease():
    global count
    count -= 1
    counter_label.config(text=str(count))

def remove():
    global count
    count = 0
    counter_label.config(text=str(count))



window=tk.Tk()
window.title("Counter")
window.geometry("1300x1500")
window.config(bg="lightblue")

count=200000000000000000000


counter_label=tk.Label(window, text=str(count), font=("berlin sans", 48))
counter_label.pack(pady=20)

increase_button=tk.Button(window,text="+", command=increase, font=("berlin sans", 24))
increase_button.pack(pady=5)

decrease_button=tk.Button(window,text="-", command=decrease, font=("berlin sans", 24))
decrease_button.pack(pady=5)

remove_button=tk.Button(window,text="Reset", command=remove, font=("berlin sans", 24))
remove_button.pack(pady=5)

window.mainloop()
