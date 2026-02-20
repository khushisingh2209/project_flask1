# databaseconnection.py
import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Khushi@123",
        database="incident_db"
    )
