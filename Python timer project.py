Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import tkinter as tk
from tkinter import messagebox
import threading
def timer_finished():
    messagebox.showinfo("Timer", "Time's up!")

def start_timer():
    global timer_event
    time = int(time_entry.get())
    timer_event = threading.Event()
    timer = threading.Timer(time, timer_finished)
    timer.start()
    remaining_time_label.config(text="Time Remaining: " + str(time) + " seconds")
    start_button.config(text="Pause", command=pause_timer)
    reset_button.config(state="normal")

    
def pause_timer():
    global timer_event
    timer_event.set()
    start_button.config(text="Resume", command=resume_timer)

    
def resume_timer():
    global timer_event
    timer_event.clear()
    start_button.config(text="Pause", command=pause_timer)

    

def reset_timer():
    global timer_event
    timer_event.set()
    start_button.config(text="Start Timer", command=start_timer)
    reset_button.config(state="disabled")
    remaining_time_label.config(text="")

    

window = tk.Tk()
window.title("Countdown Timer")
''
time_label = tk.Label(window, text="Enter time in seconds:")
time_label.pack()
SyntaxError: multiple statements found while compiling a single statement
time_label = tk.Label(window, text="Enter time in seconds:")
time_label.pack()
time_entry = tk.Entry(window)
time_entry.pack()

start_button = tk.Button(window, text="Start Timer", command=start_timer)

start_button.pack()
reset_button = tk.Button(window, text="Reset Timer", command=reset_timer, state="disabled")
reset_button.pack()
remaining_time_label = tk.Label(window)
remaining_time_label.pack()

window.mainloop()
