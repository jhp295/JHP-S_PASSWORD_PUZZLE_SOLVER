import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("jhp's Password Cracker")
root.geometry("400x300")
root.configure(bg="#1e1e1e")
root.attributes("-alpha", 0.0)  # Start fully transparent

# Animation: Fade-in
def fade_in(opacity=0.0):
    if opacity <= 1.0:
        root.attributes("-alpha", opacity)
        root.after(30, lambda: fade_in(opacity + 0.05))

# Login logic
def login():
    user = username_entry.get()
    pwd = password_entry.get()
    if user == "tahsanNafis" and pwd == "jibranisverycool12@4":
        messagebox.showinfo("Good boy....", "Logged in!")
    else:
        messagebox.showerror("Bad boy....", "Invalid credentials")

# Style + Widgets
frame = tk.Frame(root, bg="#2a2a2a", bd=0)
frame.place(relx=0.5, rely=0.5, anchor="center")

title = tk.Label(frame, text="Login", font=("Segoe UI", 20), fg="white", bg="#2a2a2a")
title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

tk.Label(frame, text="Username", fg="white", bg="#2a2a2a").grid(row=1, column=0, sticky="e")
username_entry = tk.Entry(frame, width=20)
username_entry.grid(row=1, column=1)

tk.Label(frame, text="Password", fg="white", bg="#2a2a2a").grid(row=2, column=0, sticky="e")
password_entry = tk.Entry(frame, width=20, show="*")
password_entry.grid(row=2, column=1)

login_btn = tk.Button(frame, text="Login", command=login, bg="#007acc", fg="white", activebackground="#005f99")
login_btn.grid(row=3, column=0, columnspan=2, pady=20)

# Hover animation on button
def on_enter(e):
    login_btn.config(bg="#005f99")

def on_leave(e):
    login_btn.config(bg="#007acc")

login_btn.bind("<Enter>", on_enter)
login_btn.bind("<Leave>", on_leave)

# Start the animation
fade_in()

# Run the app
root.mainloop()
