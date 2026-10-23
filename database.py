import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Hemalatha@1407",
        database="employee_payment"
    )
