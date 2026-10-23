from tkinter import *
from tkinter import messagebox
from database import get_connection
from register import open_register
from dashboard import open_dashboard


def start_login():

    root = Tk()
    root.title("Employee Payment System - Login")
    root.geometry("400x400")

    Label(
        root,
        text="EMPLOYEE PAYMENT SYSTEM",
        font=("Arial", 18, "bold")
    ).pack(pady=30)

    Label(
        root,
        text="Username",
        font=("Arial", 12)
    ).pack()

    username = Entry(root, width=30)
    username.pack(pady=8)

    Label(
        root,
        text="Password",
        font=("Arial", 12)
    ).pack()

    password = Entry(root, width=30, show="*")
    password.pack(pady=8)

    def login():

        user = username.get()
        pwd = password.get()

        if user == "" or pwd == "":
            messagebox.showerror(
                "Error",
                "Enter username and password"
            )
            return

        try:

            con = get_connection()
            cur = con.cursor()

            cur.execute(
                """
                SELECT * FROM users
                WHERE username=%s AND password=%s
                """,
                (user, pwd)
            )

            result = cur.fetchone()

            cur.close()
            con.close()

            if result:

                messagebox.showinfo(
                    "Login",
                    "Login successful"
                )

                # Hide login window
                root.withdraw()

                # Open dashboard
                open_dashboard(root, user)

            else:

                messagebox.showerror(
                    "Login Failed",
                    "Invalid username or password"
                )

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

    Button(
        root,
        text="LOGIN",
        width=20,
        height=2,
        command=login
    ).pack(pady=20)

    Button(
        root,
        text="REGISTER",
        width=20,
        height=2,
        command=open_register
    ).pack()

    root.mainloop()


if __name__ == "__main__":
    start_login()
