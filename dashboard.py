
from tkinter import *
from tkinter import messagebox

from employee import open_employee
from payment import open_payment
from history import open_history
from report import open_report


def open_dashboard(login_window, username):

    dashboard = Toplevel(login_window)
    dashboard.title("Employee Payment System - Dashboard")
    dashboard.geometry("900x600")
    dashboard.resizable(False, False)

    # Header
    Label(
        dashboard,
        text="EMPLOYEE PAYMENT SYSTEM",
        font=("Arial", 24, "bold")
    ).pack(pady=25)

    Label(
        dashboard,
        text=f"Welcome, {username}",
        font=("Arial", 14)
    ).pack(pady=5)

    # Dashboard buttons
    frame = Frame(dashboard)
    frame.pack(pady=40)

    Button(
        frame,
        text="EMPLOYEE MANAGEMENT",
        width=25,
        height=2,
        command=lambda: open_employee(dashboard)
    ).grid(row=0, column=0, padx=20, pady=15)

    Button(
        frame,
        text="SALARY PAYMENT",
        width=25,
        height=2,
        command=lambda: open_payment(dashboard)
    ).grid(row=0, column=1, padx=20, pady=15)

    Button(
        frame,
        text="PAYMENT HISTORY",
        width=25,
        height=2,
        command=lambda: open_history(dashboard)
    ).grid(row=1, column=0, padx=20, pady=15)

    Button(
        frame,
        text="REPORT",
        width=25,
        height=2,
        command=lambda: open_report(dashboard)
    ).grid(row=1, column=1, padx=20, pady=15)

    # Logout function
    def logout():
        dashboard.destroy()
        login_window.deiconify()

    Button(
        dashboard,
        text="LOGOUT",
        width=20,
        height=2,
        command=logout
    ).pack(pady=30)

    # Handle window close
    dashboard.protocol("WM_DELETE_WINDOW", logout)

    dashboard.deiconify()
    dashboard.lift()

