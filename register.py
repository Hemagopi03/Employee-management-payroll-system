from tkinter import *
from tkinter import messagebox
from database import get_connection


def open_register():

    root = Toplevel()
    root.title("Employee Payment System - Register")
    root.geometry("400x350")

    Label(root, text="REGISTER",
          font=("Arial", 20, "bold")).pack(pady=20)

    Label(root, text="Username").pack()
    username = Entry(root, width=30)
    username.pack(pady=5)

    Label(root, text="Password").pack()
    password = Entry(root, width=30, show="*")
    password.pack(pady=5)

    Label(root, text="Confirm Password").pack()
    confirm = Entry(root, width=30, show="*")
    confirm.pack(pady=5)

    def register():

        user = username.get()
        pwd = password.get()
        cpwd = confirm.get()

        if user == "" or pwd == "":
            messagebox.showerror("Error", "All fields are required")
            return

        if pwd != cpwd:
            messagebox.showerror("Error", "Passwords do not match")
            return

        try:
            con = get_connection()
            cur = con.cursor()

            cur.execute(
                "INSERT INTO users(username,password) VALUES(%s,%s)",
                (user, pwd)
            )

            con.commit()

            messagebox.showinfo(
                "Success",
                "Registration successful"
            )

            root.destroy()

        except Exception as e:
            messagebox.showerror("Error", str(e))

        finally:
            try:
                cur.close()
                con.close()
            except:
                pass

    Button(root,
           text="REGISTER",
           width=20,
           command=register).pack(pady=20)
