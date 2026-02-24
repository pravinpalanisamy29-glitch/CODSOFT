import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
import os

# Main Window
root = tk.Tk()
root.title("✨ My To-Do List")
root.geometry("500x600")
root.config(bg="#1e1e2f")

# Title Label
title = tk.Label(root, text="📝 My Daily Tasks", 
                 font=("Helvetica", 20, "bold"), 
                 bg="#1e1e2f", fg="#ffffff")
title.pack(pady=20)

# Frame for Entry
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=25, font=("Helvetica", 14))
task_entry.grid(row=0, column=0, padx=10)

def add_task():
    task = task_entry.get()
    if task != "":
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

add_btn = tk.Button(frame, text="Add Task", 
                    command=add_task,
                    bg="#4CAF50", fg="white",
                    font=("Helvetica", 12, "bold"))
add_btn.grid(row=0, column=1)

# Listbox
task_list = tk.Listbox(root, width=40, height=15, 
                       font=("Helvetica", 14),
                       bg="#2e2e3f", fg="white",
                       selectbackground="#6c63ff")
task_list.pack(pady=20)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=10)

def delete_task():
    try:
        selected = task_list.curselection()
        task_list.delete(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task!")

def mark_complete():
    try:
        selected = task_list.curselection()
        task = task_list.get(selected)
        task_list.delete(selected)
        task_list.insert(tk.END, "✔ " + task)
    except:
        messagebox.showwarning("Warning", "Please select a task!")

def clear_tasks():
    task_list.delete(0, tk.END)

delete_btn = tk.Button(btn_frame, text="Delete Task",
                       command=delete_task,
                       bg="#f44336", fg="white",
                       font=("Helvetica", 12, "bold"))
delete_btn.grid(row=0, column=0, padx=5)

complete_btn = tk.Button(btn_frame, text="Mark Complete",
                         command=mark_complete,
                         bg="#2196F3", fg="white",
                         font=("Helvetica", 12, "bold"))
complete_btn.grid(row=0, column=1, padx=5)

clear_btn = tk.Button(btn_frame, text="Clear All",
                      command=clear_tasks,
                      bg="#ff9800", fg="white",
                      font=("Helvetica", 12, "bold"))
clear_btn.grid(row=0, column=2, padx=5)

root.mainloop()
def save_tasks():
    tasks = task_list.get(0, tk.END)
    with open("tasks.json", "w") as f:
        json.dump(list(tasks), f)

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
            for task in tasks:
                task_list.insert(tk.END, task)

load_tasks()
root.protocol("WM_DELETE_WINDOW", lambda: (save_tasks(), root.destroy()))