# #A password generator is a useful tool that generates strong and random passwords for users
#This project aims to create a password generator application using Python, allowing users to
# specify the length and complexity of the password.
from tkinter import *
import random
import string

window = Tk()
window.title("Password Generator")
window.config(pady =100,padx=100, bg='#E2DAD6')

input_length = Entry(width = 25, borderwidth=1, relief="solid")
input_length.grid(column = 1, row = 1, ipadx=5, ipady=5)
input_label = Label(window, text = "Password length", bg='#E2DAD6',fg = "#543310", font=("Helvetica", 12, "bold"))
input_label.grid(column = 1, row = 0)

label_password = Label(window, text = "Generated password will appear here", bg='#E2DAD6', font=("Helvetica", 12))
label_password.config(padx=10, pady=20, font=("Helvetica", 12, "bold"))

label_strength = Label(window, text = "Password strength will appear here", bg='#E2DAD6', font=("Helvetica", 12))
label_strength.config(padx=10, pady=10, font=("Helvetica", 12, "bold"))

def password_generate():
    try:
        user_input = int(input_length.get())
        if user_input <= 0:
            raise ValueError("Length of password should be a positive number.")
    except ValueError as e:
        #hiding labels if input is invalid
        label_password.grid_remove()
        label_strength.grid_remove()
        return
    
    label_password.grid(column=1, row=3, pady=10)
    label_strength.grid(column=1, row=4, pady=10)


    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=user_input))

    label_password.config(text=f"Generated password is: {password}", font=("Helvetica", 12, "bold"))


    if len(password) < 8:
        strength = "Password strength: Weak ☹.\nFor more security,\nchoose a password of 12 characters or more."
    elif 8 <= len(password) < 12:
        strength = "Password strength: Medium 🙂.\nFor more security,\nchoose a password of 12 characters or more."
    else:
        if has_reqd_complexity(password):
            strength = "Password strength: Excellent ☺"
        else:
            strength = "Password strength: Medium 🙂\n" \
                       "For more security, ensure your password includes a mix of uppercase letters,\nlowercase letters, digits, and special characters."

    label_strength.config(text=strength, font=("Helvetica", 12, "bold"))



def has_reqd_complexity(my_password):
    return (any(c.islower() for c in my_password) and
            any(c.isupper() for c in my_password) and
            any(c.isdigit() for c in my_password) and
            any(c in string.punctuation for c in my_password))


generate_btn = Button(window, command= password_generate, text = "Generate Password", bg='#BC9F8B', fg='white', 
                      font=("Helvetica", 12, "bold"), padx=10, pady=5)
generate_btn.grid(column=1, row=2, pady=20)
generate_btn.config(pady=5, padx = 20, font= ("Arial", 12, "bold"))


window.mainloop()




