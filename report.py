
from tkinter import *
from tkinter import messagebox


def open_report(parent):
    win = Toplevel(parent)
    win.title("Payroll Report")
    win.geometry("500x350")

    Label(
        win, text="PAYROLL REPORT",
        font=("Arial", 20, "bold")
    ).pack(pady=25)

    try:
        from database import get_connection
        con = get_connection()
        cur = con.cursor()

        cur.execute("SELECT COUNT(*) FROM employees")
        employees = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM payments")
        payments = cur.fetchone()[0]

        cur.execute("SELECT COALESCE(SUM(net_salary), 0) FROM payments")
        total = cur.fetchone()[0]

        cur.close()
        con.close()

        Label(win, text=f"Total Employees: {employees}",
              font=("Arial", 14)).pack(pady=10)

        Label(win, text=f"Total Payments: {payments}",
              font=("Arial", 14)).pack(pady=10)

        Label(win, text=f"Total Net Salary Paid: ₹{total:.2f}",
              font=("Arial", 14)).pack(pady=10)

    except Exception as e:
        messagebox.showerror("Database Error", str(e))
