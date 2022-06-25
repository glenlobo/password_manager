from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    data = f'{website_input.get()} | {email_input.get()} | {password_input.get()}\n'

    with open("data.txt", 'a') as file:
        file.write(data)
        website_input.delete(0, END)
        password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=logo_img)

website_label = Label(text="Website")
email_label = Label(text="Email/Username")
password_label = Label(text="Password")
# generate_password = Label(text="Generate Password")

website_input = Entry(width=45)
website_input.focus()
email_input = Entry(width=45)
email_input.insert(END, "glen@gmail.com")
password_input = Entry(width=25)

generate_button = Button(text="Generate Password")
add_button = Button(text="Add", width=30, command=save)

canvas.grid(row=0, column=1)
website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)
website_input.grid(row=1, column=1, columnspan=2)
email_input.grid(row=2, column=1, columnspan=2)
password_input.grid(row=3, column=1, columnspan=1)
generate_button.grid(row=3, column=2, columnspan=1)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
