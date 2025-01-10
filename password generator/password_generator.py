import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    use_specials = include_specials.get()
    
    all_chars = string.ascii_letters + string.digits
    if use_specials:
        all_chars += string.punctuation
    
    password = ''.join(random.choice(all_chars) for _ in range(length))
    password_label.config(text=password)
    copy_button.config(state=tk.NORMAL)

def copy_to_clipboard():
    password = password_label.cget("text")
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()
    copy_button.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

# Title label
tk.Label(root, text="Password Generator", font=("Helvetica", 16)).pack(pady=10)

# Length entry
tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root, width=5)
length_entry.insert(0, "12")
length_entry.pack(pady=5)

# Special characters checkbox
include_specials = tk.BooleanVar()
tk.Checkbutton(root, text="Include Special Characters", variable=include_specials).pack(pady=5)

# Generate Password Button
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# Password label
password_label = tk.Label(root, text="", font=("Helvetica", 12), fg="green")
password_label.pack(pady=5)

# Copy to Clipboard Button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, state=tk.DISABLED)
copy_button.pack(pady=5)

root.mainloop()
