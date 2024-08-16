import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry_task.get()
    if task:
        list_items.insert(tk.END, task)
        entry_task.delete(0, tk.END)
        tasks.append(task)

def remove_task():
    selected_task_index = list_items.curselection()
    if selected_task_index:
        list_items.delete(selected_task_index)

def populate_entry(event):
    selected_index = list_items.curselection()
    if selected_index:
        entry_task.delete(0, tk.END)
        selected_task = list_items.get(selected_index)
        entry_task.insert(0, selected_task)

def edit_task():
    selected_index = list_items.curselection()
    if selected_index:
        selected_index = selected_index[0]
        new_entry_text = entry_task.get()
        if new_entry_text:
            tasks[selected_index] = new_entry_text
            list_items.delete(selected_index)
            list_items.insert(selected_index, new_entry_text)
            entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty.")
    else:
        messagebox.showwarning("Selection Error", "Please select a task to edit.")

# Main window
root = tk.Tk()
root.title("My To-Do List")
root.geometry("600x600")
root.configure(bg="black")

title = tk.Label(root, text="My Tasks 📝", font=("Arial", 22), bg="black", fg="cornsilk")
title.pack(pady=20)

entry_task = tk.Entry(root, width=40, font=("Verdana", 10))
entry_task.pack(pady=40, ipady=6, ipadx=10)

list_items = tk.Listbox(root, width=50, height=20, font=("Arial", 10), selectbackground="black", selectforeground="white")
list_items.pack(pady=10)
list_items.bind('<<ListboxSelect>>', populate_entry)

frame = tk.Frame(root, bg="black")
frame.pack(pady=10, padx=10)

add_btn = tk.Button(frame, text="Add task", command=add_task, font=("Arial", 12), bg="black", fg="cornsilk", cursor="hand2")
add_btn.pack(side=tk.LEFT, ipady=10, padx=10)

remove_btn = tk.Button(frame, text="Remove task", command=remove_task, font=("Arial", 12), bg="black", fg="cornsilk", cursor="hand2")
remove_btn.pack(side=tk.RIGHT, ipady=10, padx=10)

edit_btn = tk.Button(frame, text="Edit task", command=edit_task, font=("Arial", 12), bg="black", fg="cornsilk", cursor="hand2")
edit_btn.pack(side=tk.RIGHT, ipady=10, padx=10)

root.mainloop()
