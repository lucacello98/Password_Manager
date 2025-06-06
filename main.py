import tkinter
from tkinter import *
from tkinter import messagebox
import random
import string



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = string.ascii_letters  # a-z + A-Z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # !@#$%^&*()_+...

    # You can tweak the length ranges
    password_length = random.randint(12, 16)
    password_chars = random.choices(letters + digits + symbols, k=password_length)

    password = ''.join(password_chars)

    # Clear and insert into the password entry field
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    window.clipboard_clear()
    window.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        # Optional warning popup
        tkinter.messagebox.showwarning(title="Oops", message="Please make sure no field is empty.")
        return

    # Confirm before saving (optional but good UX)
    is_ok = tkinter.messagebox.askokcancel(
        title=website,
        message=f"Save the following details?\n\nEmail: {email}\nPassword: {password}"
    )

    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")

        # Clear the website and password fields
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.configure(padx=20,pady=20,bg="White")

canvas = Canvas(width=200,height=200,bg="white",highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=1,column=2)

website_label = tkinter.Label(text="Website:",bg="White",fg="black")
website_label.grid(row=2,column=1)

website_entry = Entry(bg="white",width=35,insertbackground="black",fg="black",highlightthickness=0)
website_entry.grid(row=2,column=2,columnspan=2)
website_entry.focus()

email_label = tkinter.Label(text="Email/username:",bg="White",fg="Black")
email_label.grid(row=3,column=1)

email_entry = Entry(bg="white",width=35,insertbackground="black",fg="black",highlightthickness=0)
email_entry.grid(row=3,column=2,columnspan=2)

password_label = tkinter.Label(text="Password:",bg="White",fg="Black")
password_label.grid(row=4,column=1)

password_entry = Entry(bg="white",width=21,insertbackground="black",fg="black",highlightthickness=0)
password_entry.grid(row=4,column=2)

Generate_password = Button(bg="White",text="Generate Password",highlightbackground="White", command=generate_password)
Generate_password.grid(row=4,column=3)

Add_button = Button(bg="White",text="Add",highlightbackground="White",width=32, command=save_password)
Add_button.grid(row=5,column=2,columnspan=2)



window.mainloop()