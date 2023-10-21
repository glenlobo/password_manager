import json
from tkinter import Tk, messagebox, Canvas, END, PhotoImage, EW, Label, Button, W, Entry
import string
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = ['!', '#', '$', '&', '@', '%', '(', ')', '*']

    rand_letters_list = [choice(letters) for _ in range(randint(8, 10))]
    rand_numbers_list = [choice(numbers) for _ in range(randint(2, 4))]
    rand_symbols_list = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = rand_letters_list + rand_numbers_list + rand_symbols_list
    shuffle(password_list)
    password = ''.join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Empty filed!!!',
                            message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
                data.update(new_data)

        except FileNotFoundError:
            data = new_data

        with open('data.json', 'w') as data_file:
            json.dump(data, data_file, indent=4)

            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def search():
    website = website_input.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title=f'Data Base Error',
                             message=f'Unable to find data. \nPlease enter data before searching.')
    else:
        if website in data.keys():
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=f'Match found! for {website}',
                                message=f' Email: {email}\n\n Password: {password}')
        else:
            messagebox.showwarning(title=f'Unable to find a match',
                                   message=f'No details for {website}')


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('MyPass - Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='../images/logo.png')

canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, sticky=EW)

website_label = Label(text='Website:', anchor=W)
website_label.grid(row=1, column=0, sticky=EW, pady=5)

email_label = Label(text='Email/Username:', anchor=W)
email_label.grid(row=2, column=0, sticky=EW, pady=5)

password_label = Label(text='Password:', anchor=W)
password_label.grid(row=3, column=0, sticky=EW, pady=5)

website_input = Entry(width=25)
website_input.grid(row=1, column=1, columnspan=1, sticky=EW, padx=10)
website_input.focus()

email_input = Entry(width=45)
email_input.grid(row=2, column=1, columnspan=2, sticky=EW, padx=10)
email_input.insert(END, 'glen@gmail.com')

password_input = Entry(width=25)
password_input.grid(row=3, column=1, columnspan=1, sticky=EW, padx=10)

search_button = Button(text='Search', width=15, command=search)
search_button.grid(row=1, column=2, columnspan=1, sticky=EW, padx=10)

generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(row=3, column=2, columnspan=1, sticky=EW, padx=10)

add_button = Button(text='Add', width=15, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW, padx=10)

window.mainloop()
