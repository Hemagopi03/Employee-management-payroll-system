
from tkinter import *
from tkinter import messagebox
from datetime import date


def open_payment(parent):
    win = Toplevel(parent)
    win.title("Salary Payment")
    win.geometry("500x500")

    Label(
        win, text="SALARY PAYMENT",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    fields = [
        "Employee ID", "Payment Month",
        "Basic Salary", "Allowance", "Deduction"
    ]

    entries = {}

    for field in fields:
        Label(win, text=field).pack()
        entry = Entry(win, width=30)
        entry.pack(pady=4)
        entries[field] = entry

    def save_payment():
        con = None
        cur = None

        try:
            employee_id = int(entries["Employee ID"].get())
            month = entries["Payment Month"].get().strip()
            basic = float(entries["Basic Salary"].get())
            allowance = float(entries["Allowance"].get() or 0)
            deduction = float(entries["Deduction"].get() or 0)

            if not month or min(basic, allowance, deduction) < 0:
                messagebox.showerror(
                    "Error", "Enter valid payment details"
                )
                return

            net = basic + allowance - deduction

            if net < 0:
                messagebox.showerror(
                    "Error", "Deduction cannot exceed gross salary"
                )
                return

            from database import get_connection
            con = get_connection()
            cur = con.cursor()

            cur.execute(
                "SELECT id FROM employees WHERE id=%s",
                (employee_id,)
            )

            if cur.fetchone() is None:
                messagebox.showerror("Error", "Employee ID not found")
                return

            cur.execute("""
                INSERT INTO payments
                (employee_id, payment_month, basic_salary,
                 allowance, deduction, net_salary, payment_date)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                employee_id, month, basic,
                allowance, deduction, net, date.today()
            ))

            con.commit()

            messagebox.showinfo(
                "Payment Saved",
                f"Net salary: ₹{net:.2f}"
            )
            win.destroy()

        except ValueError:
            messagebox.showerror("Error", "Check the numeric values")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            if cur:
                cur.close()
            if con:
                con.close()

    Button(
        win, text="SAVE PAYMENT",
        width=20, command=save_payment
    ).pack(pady=20)
