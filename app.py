import sqlite3

with sqlite3.connect('hospital.db') as db:
    cursor = db.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS workers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL,
        phone_number VARCHAR(255)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS receipts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content VARCHAR(255) NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        worker_id INTEGER NOT NULL,
        date TIMESTAMP NOT NULL,
        FOREIGN KEY (worker_id) REFERENCES workers(id)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL,
        phone_number VARCHAR(255),
        appointment_id INTEGER,
        receipt_id INTEGER,
        FOREIGN KEY (appointment_id) REFERENCES appointments(id),
        FOREIGN KEY (receipt_id) REFERENCES receipts(id)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history_of_visits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        appointment_id INTEGER NOT NULL,
        patient_id INTEGER NOT NULL,
        date TIMESTAMP NOT NULL,
        receipt_id INTEGER,
        FOREIGN KEY (appointment_id) REFERENCES appointments(id),
        FOREIGN KEY (patient_id) REFERENCES patients(id),
        FOREIGN KEY (receipt_id) REFERENCES receipts(id)
    );
    """)

    db.commit()