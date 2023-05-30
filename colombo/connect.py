import mysql.connector

data_base = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='colombo'
)

cursor = data_base.cursor()