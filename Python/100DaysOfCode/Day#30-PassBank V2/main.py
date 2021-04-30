from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

version = "1.0"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def new_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    pass_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = site_entry.get()
    email = user_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title='Blank Fields', message="Please don't leave any fields blank!")

    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)

            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            site_entry.delete(0, END)
            pass_entry.delete(0, END)


# ----------------------------- SEARCH ---------------------------------#
def search():
    website = site_entry.get()
    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message="No data file found.")

    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")

        else:
            messagebox.showinfo(title='Error', message='No detail for that website.')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title(f"PassBank Ver:{version}")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock)
canvas.grid(column=1, row=0)

site_label = Label(text='Website:', font=('Courier', 10, 'normal'))
site_label.grid(column=0, row=1)
name_label = Label(text='Email/Username:', font=('Courier', 10, 'normal'))
name_label.grid(column=0, row=2)
pass_label = Label(text='Password:', font=('Courier', 10, 'normal'))
pass_label.grid(column=0, row=3)

site_entry = Entry(width=20)
site_entry.grid(column=1, row=1)
site_entry.focus()
user_entry = Entry(width=35)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, '')
pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)

gene_button = Button(text='Generate Password', command=new_pass)
gene_button.grid(column=2, row=3)
add_button = Button(width=36, text='Add', command=save, font=('Courier', 10, 'normal'))
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text='Search', command=search, width=13)
search_button.grid(column=2, row=1)

window.mainloop()
