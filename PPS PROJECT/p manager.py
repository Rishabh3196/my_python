from tkinter import *

root = Tk()

root.title("PASSWORD MANAGER")
root.geometry("800x800")


def confirm():
    page2 = Toplevel(root)

    enter_masterpassword.destroy()
    enter_masterpassword_name.destroy()
    enter_masterpassword_button.destroy()

    def add():
        page3 = Toplevel(root)

        add_password.destroy()
        update_password.destroy()
        remove_password.destroy()
        show_password.destroy()
        back_button_1.destroy()

        global s
        global username_entry
        global password_entry

        username_1 = Label(page3, text="USERNAME", padx=25, pady=20)
        username_1.grid(row=1, column=1, columnspan=1)

        username_password_1 = Label(page3, text="PASSWORD", padx=25, pady=20)
        username_password_1.grid(row=2, column=1, columnspan=1)

        username_2 = Entry(page3, width=50)
        username_2.grid(row=1, column=3)

        username_password_2 = Entry(page3, width=50)
        username_password_2.grid(row=2, column=3)

        def save():
            global s
            global storage
            username_entry = username_2.get()
            password_entry = username_password_2.get()
            storage = {}
            storage[username_entry] = password_entry

            import json
            s = json.dumps(storage)

            with open("C:/Users/yrohi/Desktop/password/1.txt", "a") as f:
                f.write(s)

        save_password = Button(page3, text="SAVE", command=save, padx=200, pady=20)
        save_password.grid(row=3, column=1, columnspan=3)

        def back_2():
            username_1.destroy()
            username_2.destroy()
            username_password_1.destroy()
            username_password_2.destroy()
            save_password.destroy()
            back_button_2.destroy()
            confirm()

        back_button_2 = Button(page3, text="BACK", command=back_2, padx=200, pady=20)
        back_button_2.grid(row=5, column=1, columnspan=3)

    def update():
        page4 = Toplevel(root)

        add_password.destroy()
        update_password.destroy()
        remove_password.destroy()
        show_password.destroy()
        back_button_1.destroy()

        global username_entry
        global password_entry

        username_1 = Label(page4, text="USERNAME", padx=25, pady=20)
        username_1.grid(row=1, column=1, columnspan=1)

        username_password_1 = Label(page4, text="PASSWORD", padx=25, pady=20)
        username_password_1.grid(row=2, column=1, columnspan=1)

        username_2 = Entry(page4, width=50)
        username_2.grid(row=1, column=3)

        username_password_2 = Entry(page4, width=50)
        username_password_2.grid(row=2, column=3)

        def save():
            global storage
            username_entry = username_2.get()
            password_entry = username_password_2.get()
            storage = {}
            storage[username_entry] = password_entry
            import json
            s = json.dumps(storage)
            with open("C:/Users/yrohi/Desktop/password/1.txt", "w") as f:
                f.write(s)

        save_password = Button(page4, text="SAVE", command=save, padx=200, pady=20)
        save_password.grid(row=3, column=1, columnspan=3)

        def back_3():
            username_1.destroy()
            username_2.destroy()
            username_password_1.destroy()
            username_password_2.destroy()
            save_password.destroy()
            back_button_3.destroy()
            confirm()

        back_button_3 = Button(page4, text="BACK", command=back_3, padx=200, pady=20)
        back_button_3.grid(row=5, column=1, columnspan=3)

    def remove():
        page5 = Toplevel(root)
        add_password.destroy()
        update_password.destroy()
        remove_password.destroy()
        show_password.destroy()
        back_button_1.destroy()

        global username_entry

        username_1 = Label(page5, text="USERNAME", padx=25, pady=20)
        username_1.grid(row=1, column=1, columnspan=1)

        username_2 = Entry(page5, width=50)
        username_2.grid(row=1, column=3)

        def save():
            global s
            global storage
            username_entry = username_2.get()
            storage = {}
            del storage[username_entry]
            import json
            s = json.dumps(storage)
            with open("C:/Users/yrohi/Desktop/password/1.txt", "r") as f:
                f.write(s)

        remove_username = Button(page5, text="REMOVE", command=save, padx=200, pady=20)
        remove_username.grid(row=2, column=1, columnspan=3)

        def back_4():
            username_1.destroy()
            username_2.destroy()
            remove_username.destroy()
            back_button_4.destroy()
            confirm()

        back_button_4 = Button(page5, text="BACK", command=back_4, padx=200, pady=20)
        back_button_4.grid(row=3, column=1, columnspan=3)

    def show():
        page6 = Toplevel(root)

        add_password.destroy()
        update_password.destroy()
        remove_password.destroy()
        show_password.destroy()
        back_button_1.destroy()

        global username_entry

        username_6_1 = Label(page6, text="USERNAME", padx=25, pady=20)
        username_6_1.grid(row=1, column=1)

        username_6_2 = Entry(page6, width=50)
        username_6_2.grid(row=1, column=2)
        username_entry = username_6_2.get()

        def show_p():
            global final_password
            global storage
            username_entry = username_6_2.get()

            import json
            with open("C:/Users/yrohi/Desktop/password/1.txt", "r") as f:
                f.read(s)
            storage = json.loads(s)
            x = storage[username_entry]

            final_password = Label(page6, text="PASSWORD : ")
            final_password.grid(row=4, column=1)

        show_password_1 = Button(page6, text="SHOW PASSWORD", command=show_p, padx=200, pady=20)
        show_password_1.grid(row=2, column=1)

        def back_5():
            final_password.destroy()
            username_6_1.destroy()
            username_6_2.destroy()
            show_password_1.destroy()
            back_button_5.destroy()
            confirm()

        back_button_5 = Button(page6, text="BACK", command=back_5, padx=200, pady=20)
        back_button_5.grid(row=3, column=1)

    add_password = Button(page2, text="ADD", command=add, padx=200, pady=20)
    add_password.grid(row=1, column=1)

    update_password = Button(page2, text="UPDATE", command=update, padx=200, pady=20)
    update_password.grid(row=2, column=1)

    remove_password = Button(page2, text="REMOVE", padx=200, command=remove, pady=20)
    remove_password.grid(row=3, column=1)

    show_password = Button(page2, text="SHOW", command=show, padx=200, pady=20)
    show_password.grid(row=4, column=1)

    def back_1():
        add_password.destroy()
        update_password.destroy()
        remove_password.destroy()
        show_password.destroy()
        back_button_1.destroy()

    back_button_1 = Button(page2, text="BACK", command=back_1, padx=200, pady=20)
    back_button_1.grid(row=5, column=1)


enter_masterpassword = Entry(root, width=30)
enter_masterpassword.grid(column=3, row=1)

enter_masterpassword_name = Label(root, text="Enter Master Password", padx=20, pady=20)
enter_masterpassword_name.grid(column=1, row=1)

enter_masterpassword_button = Button(root, text="confirm", padx=20, pady=20, command=confirm)
enter_masterpassword_button.grid(column=3, row=2, columnspan=2)

root.mainloop()