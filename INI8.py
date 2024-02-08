import sqlite3
from datetime import datetime

class RegistrationDatabase:
    def __init__(self, db_name='registration.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Registration (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Email TEXT NOT NULL,
                DateOfBirth DATE
            )
        ''')
        self.conn.commit()

    def create_record(self, name, email, date_of_birth):
        try:
            self.cursor.execute('''
                INSERT INTO Registration (Name, Email, DateOfBirth)
                VALUES (?, ?, ?)
            ''', (name, email, date_of_birth))
            self.conn.commit()
            print("Record created successfully.")
        except sqlite3.Error as e:
            print(f"Error creating record: {e}")

    def read_records(self):
        try:
            self.cursor.execute('SELECT * FROM Registration')
            records = self.cursor.fetchall()
            for record in records:
                print(record)
        except sqlite3.Error as e:
            print(f"Error reading records: {e}")

    def update_record(self, record_id, new_name, new_email, new_date_of_birth):
        try:
            self.cursor.execute('''
                UPDATE Registration
                SET Name = ?, Email = ?, DateOfBirth = ?
                WHERE ID = ?
            ''', (new_name, new_email, new_date_of_birth, record_id))
            self.conn.commit()
            print("Record updated successfully.")
        except sqlite3.Error as e:
            print(f"Error updating record: {e}")

    def delete_record(self, record_id):
        try:
            self.cursor.execute('DELETE FROM Registration WHERE ID = ?', (record_id,))
            self.conn.commit()
            print("Record deleted successfully.")
        except sqlite3.Error as e:
            print(f"Error deleting record: {e}")

    def close_connection(self):
        self.conn.close()

# Example usage:

# Create an instance of the RegistrationDatabase
registration_db = RegistrationDatabase()

# Create a record
registration_db.create_record("John Doe", "john.doe@example.com", "1990-01-01")

# Read all records
registration_db.read_records()

# Update a record
registration_db.update_record(1, "John Updated", "john.updated@example.com", "1990-02-02")

# Read all records after update
registration_db.read_records()

# Delete a record
registration_db.delete_record(1)

# Read all records after delete
registration_db.read_records()

# Close the connection
registration_db.close_connection()
