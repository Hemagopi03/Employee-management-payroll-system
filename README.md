# Employee Management and Payroll System

A desktop-based Employee Management and Payroll System developed using **Python, Tkinter, and MySQL**. This application helps manage employee information, process salary payments, and generate payroll reports through a simple graphical user interface.

## 🚀 Project Overview

The Employee Management and Payroll System is designed to simplify employee data management and salary processing. It uses Python Tkinter for the frontend and MySQL as the backend database.

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **GUI Framework:** Tkinter
- **Database:** MySQL
- **Database Connector:** MySQL Connector/Python
- **IDE:** IDLE
- **Database Tool:** MySQL Workbench

## ✨ Features

- User Registration
- User Login Authentication
- Dashboard Interface
- Employee Information Management
- Employee Data Insertion
- Salary Payment Management
- Automatic Net Salary Calculation
- Payment History
- Payroll Report Generation
- MySQL Database Integration

## 💰 Salary Calculation

The system calculates net salary using the following formula:

**Net Salary = Basic Salary + Allowance - Deduction**

## 📂 Project Structure

```text
Employee-management-payroll-system/
│
├── main.py
├── login.py
├── register.py
├── dashboard.py
├── employee.py
├── payment.py
├── history.py
├── report.py
├── database.py
│
├── employee_payment.sql
├── README.md
└── requirements.txt
```

## ⚙️ Installation and Setup

### Step 1: Install Python

Download and install Python 3 from:

https://www.python.org/downloads/

### Step 2: Install MySQL

Install MySQL Server and MySQL Workbench.

### Step 3: Clone the Repository

```bash
git clone https://github.com/Hemagopi03/Employee-management-payroll-system.git
```

### Step 4: Open the Project

```bash
cd Employee-management-payroll-system
```

### Step 5: Install Required Packages

```bash
pip install -r requirements.txt
```

### Step 6: Configure MySQL Database

1. Open MySQL Workbench.
2. Connect to your MySQL server.
3. Import and execute the `employee_payment.sql` file.
4. Configure the database connection details in `database.py`.

### Step 7: Run the Application

```bash
python main.py
```

## 🗄️ Database

**Database Name:** `employee_payment`

The application uses MySQL to store employee information, user login details, and salary payment records.

## 🎯 Learning Outcomes

- Understanding Core Python Programming
- Developing GUI Applications using Tkinter
- Connecting Python with MySQL
- Performing Database Operations
- Implementing Salary Calculation Logic
- Generating Payroll Reports

## 👩‍💻 Developer

**Hemalatha Balakumar**

B.E. Computer Science and Engineering

GitHub: https://github.com/Hemagopi03


---

⭐ If you find this project useful, feel free to explore the repository and share your feedback.

**Thank you for visiting my project!**
