
import tkinter as Tk
from tkinter import font
 
 
window = Tk.Tk()
 
window.title("Note taking app")
 
window.geometry("1500x900")
 
window.config(bg="silver")
 
def show_frame1():
    frame3.pack_forget()
    frame2.pack_forget()
    frame4.pack_forget()
    frame1_container.pack(fill="both", expand=True)  

def show_frame2():
    frame1_container.pack_forget()  
    frame3.pack_forget()
    frame4.pack_forget()
    frame2.pack(fill="both", expand=True)

def show_frame3():
    frame1_container.pack_forget()  
    frame2.pack_forget()
    frame4.pack_forget()
    frame3.pack(fill="both", expand=True)

def show_frame4():
    frame1_container.pack_forget()  
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack(fill="both", expand=True)



frame2 = Tk.Frame(window, bg="lightgrey")
frame3 = Tk.Frame(window, bg="lightgrey")
frame4 = Tk.Frame(window, bg="lightgrey")




frame1_container = Tk.Frame(window, bg="lightgrey")
frame1_container.pack(fill="both", expand=True)

scrollbar = Tk.Scrollbar(frame1_container, orient="vertical")
scrollbar.pack(side="right", fill="y")


canvas = Tk.Canvas(frame1_container, bg="lightgrey", highlightthickness=0)
canvas.pack(side="left", fill="both", expand=True)


canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=canvas.yview)

frame1 = Tk.Frame(canvas, bg="lightgrey")
canvas_window = canvas.create_window((0, 0), window=frame1, anchor="nw")

def on_frame1_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame1.bind("<Configure>", on_frame1_configure)

def on_canvas_configure(event):
    canvas.itemconfig(canvas_window, width=event.width)

canvas.bind("<Configure>", on_canvas_configure)

def on_canvas_configure(event):
    canvas.itemconfig(canvas_window, width=event.width)

canvas.bind("<Configure>", on_canvas_configure)


def on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

def bind_mousewheel(event):
    canvas.bind_all("<MouseWheel>", on_mousewheel)

def unbind_mousewheel(event):
    canvas.unbind_all("<MouseWheel>")


frame1_container.bind("<Enter>", bind_mousewheel)
frame1_container.bind("<Leave>", unbind_mousewheel)

frame2 = Tk.Frame(window, bg="lightgrey")
frame3 = Tk.Frame(window, bg="lightgrey")
frame4 = Tk.Frame(window, bg="lightgrey")
 
bold_font = font.Font(family="Helvetica", size=16, weight="bold")
 
title_label = Tk.Label(frame1, text="Welcome to Note Every ", font=bold_font, bg="lightgrey")
title_label.pack(pady=20)
 
welcome_label = Tk.Label(frame1, text="Click on the buttons below to navigate", bg="lightgrey")
welcome_label.pack(pady=10)
 
separator = Tk.Frame(frame1, bg = "gray", height=2)
separator.pack(fill="x", padx=20, pady=10)
button4 = Tk.Button(frame1, text="Get Started", bg="#2056f7", fg="#ffffff", command=show_frame2, padx=30, pady=15, font=("Helvetica", 12), relief="flat", bd=0)
button4.pack(pady=20)
 
separator = Tk.Frame(frame1, bg = "gray", height=2)
separator.pack(fill="x", padx=20, pady=10)
 
manage_label=Tk.Label(frame1 , text="Easy management",font=bold_font, bg="lightgrey",fg="black")
manage_label.pack(pady=20)
 
checklist_img = Tk.PhotoImage(file="Clipboard-2-64.png")
checklist_img_label = Tk.Label(frame1, image=checklist_img, bg="lightgrey")
checklist_img_label.pack(pady=20)
 
manage_label2=Tk.Label(frame1 , text="Add, organize, and track your tasks with a clean and intuitive interface",font="arial",bg="lightgrey")
manage_label2.pack(pady=20)
 
separator = Tk.Frame(frame1, bg = "gray", height=2)
separator.pack(fill="x", padx=20, pady=10)
 
track_progress_label=Tk.Label(frame1 ,text="Track Progress",font=bold_font, bg="lightgrey")
track_progress_label.pack(pady=20)
 
tick_img = Tk.PhotoImage(file="checked-checkbox-64.png")
tick_img_label = Tk.Label(frame1, image=tick_img, bg="lightgrey")
tick_img_label.pack(pady=20)
 
track_progress_label2=Tk.Label(frame1,text="Mark tasks as complete and see your productivity at a glance",font="arial",bg="lightgrey")
track_progress_label2.pack(pady=20)
 
separator = Tk.Frame(frame1, bg = "gray", height=2)
separator.pack(fill="x", padx=20, pady=10)
 
customizable_label=Tk.Label(frame1,text="Customizable",font=bold_font, bg="lightgrey")
customizable_label.pack(pady=20)
 
settings_img = Tk.PhotoImage(file="settings-17-64.png")
settings_img_label = Tk.Label(frame1, image=settings_img, bg="lightgrey")
settings_img_label.pack(pady=20)
 
 
customizable_label2=Tk.Label(frame1,text="Personalize your experience with dark mode and custom settings,",font="arial",bg="lightgrey")
customizable_label2.pack(pady=20)
 
button_frame = Tk.Frame(window, bg="silver")
button_frame.pack(side="bottom", fill="both")
 

settings_image = Tk.PhotoImage(file="settings.png")
button_settings = Tk.Button(button_frame, image=settings_image, command=show_frame4)
button_settings.image = settings_image  
button_settings.pack(side="left", padx=10, pady=10, expand=True, fill="both")

task_image = Tk.PhotoImage(file="tasks.png") 
button_task = Tk.Button(button_frame, image=task_image, command=show_frame3) 
button_task.image = task_image  
button_task.pack(side="left", padx=10, pady=10, expand=True, fill="both")

stats_image = Tk.PhotoImage(file="bar-chart.png")
button_stats= Tk.Button(button_frame, image=stats_image, command=show_frame2)
button_stats.image = settings_image  
button_stats.pack(side="left", padx=10, pady=10, expand=True, fill="both")


home_image = Tk.PhotoImage(file="home.png")
button_home = Tk.Button(button_frame, image=home_image, command=show_frame1)
button_home.image = home_image
button_home.pack(side="left", padx=10, pady=10, expand=True, fill="both")

settings_title = Tk.Label(frame4, text="Settings", font=bold_font, bg="lightgrey", anchor="w")
settings_title.pack(fill="x", padx=20, pady=20)

separator = Tk.Frame(frame4, bg = "gray", height=2)
separator.pack(fill="x", padx=20, pady=10)

settings_darkmode=Tk.Label(frame4, text="Darkmode toggle",font="arial",bg="lightgrey",anchor="w")
settings_darkmode.pack(fill="x", padx=20,pady=20)




show_frame1()
window.mainloop()

# frame 1 = home 
# frame 2 = stats
# frame 3 = tasks
# frame 4 = settings
