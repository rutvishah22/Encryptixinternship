import tkinter as tk
import math

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y


def modulus(x, y):
    return x % y


def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def click(event):
    global expression
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(expression))  # Evaluate the expression
            display_var.set(result)
            expression = result
        except Exception as e:
            display_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        display_var.set("")
    elif text == "√":
        try:
            result = str(square_root(float(expression)))
            display_var.set(result)
            expression = result
        except Exception as e:
            display_var.set("Error")
            expression = ""
    else:
        expression += text
        display_var.set(expression)

expression = ""

root = tk.Tk()
root.title("My Calculator")

display_var = tk.StringVar()
display = tk.Entry(root, textvar=display_var, font="lucida 20 bold")
display.pack(fill=tk.BOTH, ipadx=8, padx=10, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C", "√", "**", "%"
]


frame = tk.Frame(root)
for i, btn in enumerate(buttons):
    button = tk.Button(frame, text=btn, font="lucida 15 bold")
    button.grid(row=i // 4, column=i % 4, padx=5, pady=5, ipadx=10, ipady=10)
    button.bind("<Button-1>", click)
frame.pack()


root.mainloop()
