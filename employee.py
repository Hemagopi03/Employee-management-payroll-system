
from tkinter import *
from tkinter import messagebox


def open_employee(parent):
    win = Toplevel(parent)
    win.title("Employee Management")
    win.geometry("600x450")

    Label(
        win,
        text="EMPLOYEE MANAGEMENT",
        font=("Arial", 20, "bold")
    ).pack(pady=20)

    labels = ["Employee Name", "Phone", "Email",
              "Department", "Designation", "Basic Salary"]

    entries = {}

    for item in labels:
        Label(win, text=item).pack()
        entry = Entry(win, width=35)
        entry.pack(pady=3)
        entries[item] = entry

    def save_employee():
        try:
            from database import get_connection

            name = entries["Employee Name"].get().strip()
            if not name:
                messagebox.showerror("Error", "Enter employee name")
                return

            salary = entries["Basic Salary"].get().strip() or "0"
            salary = float(salary)

            con = get_connection()
            cur = con.cursor()

            cur.execute("""
                INSERT INTO employees
                (name, phone, email, department, designation, basic_salary)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                name,
                entries["Phone"].get(),
                entries["Email"].get(),
                entries["Department"].get(),
                entries["Designation"].get(),
                salary
            ))

            con.commit()
            cur.close()
            con.close()

            messagebox.showinfo("Success", "Employee saved")
            win.destroy()

        except ValueError:
            messagebox.showerror("Error", "Enter a valid salary")
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    Button(
        win, text="SAVE EMPLOYEE",
        width=20, command=save_employee
    ).pack(pady=15)
