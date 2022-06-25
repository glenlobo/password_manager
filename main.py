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
canvas.grid(row=0, column=1, sticky=EW)

website_label = Label(text="Website:", anchor=W)
website_label.grid(row=1, column=0, sticky=EW, pady=5)

email_label = Label(text="Email/Username:", anchor=W)
email_label.grid(row=2, column=0, sticky=EW, pady=5)

password_label = Label(text="Password:", anchor=W)
password_label.grid(row=3, column=0, sticky=EW, pady=5)

website_input = Entry(width=45)
website_input.grid(row=1, column=1, columnspan=2, sticky=EW, padx=10)
website_input.focus()

email_input = Entry(width=45)
email_input.grid(row=2, column=1, columnspan=2, sticky=EW, padx=10)
email_input.insert(END, "glen@gmail.com")

password_input = Entry(width=25)
password_input.grid(row=3, column=1, columnspan=1, sticky=EW, padx=10)

generate_button = Button(text="Generate Password")
generate_button.grid(row=3, column=2, columnspan=1, sticky=EW, padx=10)

add_button = Button(text="Add", width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW, padx=10)

window.mainloop()
