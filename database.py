import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR PASSWORD HERE",
        database="employee_payment"
    )
