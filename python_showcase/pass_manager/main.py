from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import json

NUM_STR = '1234567890'
SYMBOL_STR = '!@#$%^&*()?-+=[]{}:;<>'
UPPER_STR = 'QWERTYUIOPASDFGHJKLZXCVBNM'
LOWER_STR = 'qwertyuiopasdfghjklzxcvbnm'

NUM_LIST = list(NUM_STR)
SYMBOL_LIST = list(SYMBOL_STR)
UPPER_LIST = list(UPPER_STR)
LOWER_LIST = list(LOWER_STR)


# ______________________FIND PASSWORD______________________________________#


def find_password():
    website_orig = web_entry.get()
    website = website_orig.title()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No passwords have been stored yet")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message="Info for this website not found.")


# ---------------------- PASSWORD GENERATOR ------------------------------- #


def pass_gen():
    pass_entry.delete(0, END)
    global NUM_LIST, SYMBOL_LIST, UPPER_LIST, LOWER_LIST
    new_pass_list = []
    for char in range(12):
        if char < 2:
            new_pass_list.append(random.choice(SYMBOL_LIST))
        elif 2 <= char <= 3:
            new_pass_list.append(random.choice(UPPER_LIST))
        elif 4 <= char <= 5:
            new_pass_list.append(random.choice(NUM_LIST))
        else:
            new_pass_list.append(random.choice(LOWER_LIST))
    random.shuffle(new_pass_list)
    shuff_pass = ""
    for char in new_pass_list:
        shuff_pass += char
    pass_entry.insert(0, shuff_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def write_data():
    website_orig = web_entry.get()
    website = website_orig.title()
    email_orig = email_entry.get()
    email = email_orig.title()
    password_orig = pass_entry.get()
    password = password_orig.title()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == '' or password == '':
        messagebox.showwarning(title="Warning", message="Please make sure all fields are filled out.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            # Create json file
            with open("data.json", "w") as data_file:
                # write new_data to json file
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            pyperclip.copy(password)
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ^^^ JSON section of code can be shortened, but is kept this way to understand what is happening


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=45, pady=45)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)

email = Label(text="Email/Username: ")
email.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

web_entry = Entry(width=21)
web_entry.grid(column=1, row=1)
web_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "KyleJDini@gmail.com")

pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)

gen_pass_button = Button(text="Generate Password", command=pass_gen)
gen_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=write_data)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()