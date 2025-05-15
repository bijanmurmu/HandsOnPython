import tkinter as tk
import time

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Set the window size
root.geometry("400x200")
root.resizable(False, False)

# Label to display the time
time_label = tk.Label(root, font=("calibri", 40, "bold"), background="white", foreground="black")
time_label.pack(anchor="center")

# Function to update the time
def update_time():
    current_time = time.strftime("%H:%M:%S")  # Format: Hour:Minute:Second
    time_label.config(text=current_time)  # Update the label with current time
    time_label.after(1000, update_time)  # Call this function again after 1 second

# Start the clock update
update_time()

# Run the Tkinter event loop
root.mainloop()