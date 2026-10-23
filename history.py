
from tkinter import *
from tkinter import ttk, messagebox


def open_history(parent):
    win = Toplevel(parent)
    win.title("Payment History")
    win.geometry("900x450")

    Label(
        win, text="PAYMENT HISTORY",
        font=("Arial", 20, "bold")
    ).pack(pady=15)

    columns = (
        "ID", "Employee ID", "Month",
        "Basic", "Allowance", "Deduction",
        "Net Salary", "Payment Date"
    )

    tree = ttk.Treeview(
        win, columns=columns, show="headings"
    )

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=105)

    tree.pack(fill=BOTH, expand=True, padx=10, pady=10)

    try:
        from database import get_connection
        con = get_connection()
        cur = con.cursor()

        cur.execute("""
            SELECT id, employee_id, payment_month,
                   basic_salary, allowance, deduction,
                   net_salary, payment_date
            FROM payments ORDER BY id DESC
        """)

        for row in cur.fetchall():
            tree.insert("", END, values=row)

        cur.close()
        con.close()

    except Exception as e:
        messagebox.showerror("Database Error", str(e))
