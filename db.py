import sqlite3
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from add2db import *

database_name = "1001.db"

def create_database(database_name):
    try:
        # Connect to the SQLite database (this will create the database if it doesn't exist)
        conn = sqlite3.connect(database_name)
        
        # Create a cursor object to execute SQL commands
        cursor = conn.cursor()

        # Create tables and define the schema as needed
        # Example: Creating a simple "users" table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS albums (
                id INTEGER,       
                title TEXT,
                url TEXT)
        ''')

        # Commit the changes to the database
        conn.commit()

        # Close the cursor and the connection
        cursor.close()
        conn.close()

        print(f"Database '{database_name}' created successfully.")

    except sqlite3.Error as e:
        print("Error creating the database:", str(e))

def add_to_db(count, title, url):
    try:
        # Connect to the SQLite database (this will create the database if it doesn't exist)
        conn = sqlite3.connect(database_name)
        
        sql = ('''
            INSERT INTO albums (id, title, url)
                       VALUES(?,?,?)      
        ''')  
        values = count, title, url
        # Create a cursor object to execute SQL commands
        cursor = conn.cursor()
        cursor.execute(sql, values)
       
        # Commit the changes to the database
        conn.commit()

        # Close the cursor and the connection
        cursor.close()
        conn.close()

    except sqlite3.Error as e:
        print("Error creating the database:", str(e))