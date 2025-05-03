import tkinter as tk
from tkinter import messagebox
import datetime

FILENAME = "tasks.txt"
tasks = []

# Load tasks from file
def load_tasks():
    global tasks
    try:
        with open(FILENAME, "r") as file:
            tasks = file.readlines()
    except FileNotFoundError:
        tasks = []

# Save tasks to file
def save_tasks():
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to add task
def add_task():
    task = task_entry.get()
    priority = priority_var.get()
    deadline = deadline_entry.get()

    if not task or not deadline:
        messagebox.showwarning("Warning", "Please enter task and deadline.")
        return

    try:
        datetime.datetime.strptime(deadline, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Error", "Deadline must be YYYY-MM-DD format.")
        return

    task_text = f"{task} [Priority: {priority}] [Deadline: {deadline}]"
    tasks.append(task_text)
    save_tasks()
    update_task_list()
    task_entry.delete(0, tk.END)
    deadline_entry.delete(0, tk.END)

# Function to mark as done
def mark_done():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        # If the task is not already marked as done
        if not tasks[index].startswith("✅ "):
            tasks[index] = "✅ " + tasks[index]  # Add ✅ before the task
            save_tasks()
            update_task_list()  # Refresh the task list after updating
        else:
            messagebox.showinfo("Info", "Task already marked as done.")
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as done.")

# Function to delete task
def delete_task():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        save_tasks()
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Update task list in GUI
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# GUI window setup
root = tk.Tk()
root.title("To-Do List GUI")
root.geometry("500x400")
root.config(bg="#f0f0f0")

# Task input
tk.Label(root, text="Task:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
task_entry = tk.Entry(root, width=50, font=("Arial", 12))
task_entry.pack(pady=5)

# Priority dropdown
tk.Label(root, text="Priority:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
priority_var = tk.StringVar(value="Medium")
priority_menu = tk.OptionMenu(root, priority_var, "High", "Medium", "Low")
priority_menu.pack(pady=5)

# Deadline input
tk.Label(root, text="Deadline (YYYY-MM-DD):", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
deadline_entry = tk.Entry(root, width=50, font=("Arial", 12))
deadline_entry.pack(pady=5)

# Buttons with colors
tk.Button(root, text="Add Task", command=add_task, bg="#4CAF50", fg="white", font=("Arial", 12), width=15).pack(pady=5)
tk.Button(root, text="Mark as Done", command=mark_done, bg="#2196F3", fg="white", font=("Arial", 12), width=15).pack(pady=5)
tk.Button(root, text="Delete Task", command=delete_task, bg="#f44336", fg="white", font=("Arial", 12), width=15).pack(pady=5)

# Task list display with colors
task_listbox = tk.Listbox(root, width=70, height=10, font=("Arial", 12), bg="#ffffff", selectmode=tk.SINGLE)
task_listbox.pack(pady=10)

# Load and display tasks
load_tasks()
update_task_list()

# Run the app
root.mainloop()
