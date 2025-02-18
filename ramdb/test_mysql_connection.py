import mysql.connector

# Database Configuration (Change based on your MySQL setup)
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "akash123456",  # Change this!
    "database": "employees"  # Change this!
}

try:
    # Connect to MySQL
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # List Tables
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    print("✅ Successfully Connected to MySQL!")
    print("📂 Found Tables:")
    for table in tables:
        print("   -", table[0])

    # Close Connection
    cursor.close()
    conn.close()

except Exception as e:
    print("❌ MySQL Connection Failed:", e)
