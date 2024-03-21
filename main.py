from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import subprocess
from characters import CHARACTERS


# ------------------------------VIEW PASSWORDS------------------------------- #


def open_text_editor():
    try:
        subprocess.run(['notepad.exe', 'data.txt'], check=True)
    except subprocess.CalledProcessError:
        print("Error: Unable to open text editor.")

# ------------------------------GENERATE PASSWORD----------------------------- #


def generate_password():
    pass_ent.delete(0, END)

    generated_password = ''
    for i in range(16):
        char = random.choice(CHARACTERS)
        generated_password += str(char)

    pass_ent.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------------SAVE DATA---------------------------------- #
def save_data():
    web_name = web_ent.get()
    email_name = e_u_ent.get()
    password_name = pass_ent.get()

    if len(web_name) == 0:
        messagebox.showerror(message="Website name cannot be left empty")

    elif len(password_name) < 12:
        messagebox.showwarning(message="Password too short")

    else:
        is_ok = messagebox.askokcancel(
            message=f'The Entered Details Are:\n  Website: {web_name}\n  Email/Username: {email_name}\n '
                    f'Password:   {password_name}', title='CONFIRM')

        if is_ok:
            with open('data.txt', 'a') as data:
                data.write(f'{web_name} | {email_name} | {password_name}\n')

            web_ent.delete(0, END)
            pass_ent.delete(0, END)


# ----------------------------------UI SETUP---------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=50)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=0, row=1, columnspan=3)

website = Label(text='Website', width=15, height=2)
website.grid(row=2, column=0)

web_ent = Entry(width=60)
web_ent.grid(row=2, column=1, columnspan=2)
web_ent.focus()

e_u = Label(text='Email/Username', width=15, height=2)
e_u.grid(row=3, column=0)

e_u_ent = Entry(width=60)
e_u_ent.grid(row=3, column=1, columnspan=2)
e_u_ent.insert(2, "gagandeepsingh11678@gmail.com")

password = Label(text='Password', width=15, height=2)
password.grid(row=4, column=0)

pass_ent = Entry(width=27)
pass_ent.grid(row=4, column=1)

gen_button = Button(text='Generate Password', width=27, command=generate_password)
gen_button.grid(row=4, column=2)

add_button = Button(text='ADD', width=51, command=save_data)
add_button.grid(row=5, column=1, columnspan=2)

view_pass = Button(text="View Saved Passwords", width=66, command=open_text_editor)
view_pass.grid(row=0, column=0, columnspan=3)

window.mainloop()
