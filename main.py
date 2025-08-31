# Importing the modules
from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet
import json


# Creating the root window
root = Tk()
root.title("Password Manager")
root.config(padx=100, pady=100)



# Creating the labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Creating the entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)



# Creating the encryption key
key = Fernet.generate_key()
f = Fernet(key)

# Defining the functions
def search_password():
    # Searching for the password of a website
    website = website_entry.get()
    try:
        # Reading the data from the JSON file
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        # Showing an error message if the file does not exist
        messagebox.showerror(title="Error", message="No Data File Found.")
    else:
        # Showing the password or an error message if the website is not found
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            # Decrypting the password
            decrypted_password = f.decrypt(password.encode()).decode()
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {decrypted_password}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {website} exists.")



def save_password():
    # Saving the password to the JSON file
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    # Encrypting the password
    encrypted_password = f.encrypt(password.encode()).decode()
    new_data = {
        website: {
            "email": email,
            "password": encrypted_password
        }
    }
    # Checking for empty fields
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Please don't leave any fields empty!")
    else:
        # Asking for confirmation
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                # Reading the old data from the file
                with open("passwords.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                # Creating a new file if it does not exist
                with open("passwords.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                # Updating the old data with the new data
                data.update(new_data)
                with open("passwords.json", "w") as file:
                    # Saving the updated data
                    json.dump(data, file, indent=4)
            finally:
                # Clearing the entries
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# Creating the buttons
search_button = Button(text="Search", width=13, command=search_password)
search_button.grid(row=1, column=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

# Running the main loop
root.mainloop()