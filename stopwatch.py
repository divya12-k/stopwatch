import tkinter as tk
from time import strftime, time, sleep
import threading

# Function to update the clock
def update_clock():
    while True:
        clock_label.config(text=strftime("%H:%M:%S"))
        sleep(1)

# Function to start the stopwatch
def start_stopwatch():
    global running, start_time
    if not running:
        running = True
        start_time = time() - elapsed_time
        update_stopwatch()

# Function to update the stopwatch display
def update_stopwatch():
    global elapsed_time
    while running:
        elapsed_time = time() - start_time
        stopwatch_label.config(text=f"{elapsed_time:.2f} sec")
        sleep(0.1)

# Function to stop the stopwatch
def stop_stopwatch():
    global running
    running = False

# Function to reset the stopwatch
def reset_stopwatch():
    global elapsed_time, running
    running = False
    elapsed_time = 0
    stopwatch_label.config(text="0.00 sec")

# Creating main window
root = tk.Tk()
root.title("Stopwatch & Clock")

clock_label = tk.Label(root, text="", font=("Arial", 20))
clock_label.pack()

stopwatch_label = tk.Label(root, text="0.00 sec", font=("Arial", 20))
stopwatch_label.pack()

start_button = tk.Button(root, text="Start", command=start_stopwatch)
start_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop_stopwatch)
stop_button.pack()

reset_button = tk.Button(root, text="Reset", command=reset_stopwatch)
reset_button.pack()

# Initialize stopwatch variables
running = False
elapsed_time = 0
start_time = 0

# Start clock thread
clock_thread = threading.Thread(target=update_clock, daemon=True)
clock_thread.start()

root.mainloop()
