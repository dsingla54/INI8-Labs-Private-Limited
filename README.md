# Registration Database

This Python script demonstrates CRUD operations on a 'Registration' table using SQLite.

## Overview

The `RegistrationDatabase` class manages a simple SQLite database for user registration. It allows creating, reading, updating, and deleting user records.

## Prerequisites

Ensure you have Python installed on your machine.

## Setup

1. **Clone the Repository:**
    ```bash
    git clone [https://github.com/dsingla54/INI8-Labs-Private-Limited]
    cd registration-database
    ```

2. **Run the Script:**
    ```bash
    python registration.py
    ```

3. **Interact with the Database:**
   - The script will guide you through creating, reading, updating, and deleting user records.
   - View the console output for the results of each operation.

4. **Optional Inspection:**
   - Inspect the 'registration.db' SQLite database file to check the data.

5. **Close the Script:**
   - When finished, close the script using:
     ```bash
     CTRL+C
     ```

## Example Usage

```python
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
