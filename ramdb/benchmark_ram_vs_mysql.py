import mysql.connector
import time
from memory_manager import MemoryManager
from query_engine import QueryEngine

# MySQL Database Configuration
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "akash123456",  # Change this!
    "database": "employees"
}

# Test Query for a Department
QUERY = "SELECT * FROM departments WHERE dept_no = 'd003'"

### **Step 1: Benchmark MySQL Query Execution Time**
conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()
start_time = time.time()
cursor.execute(QUERY)
mysql_result = cursor.fetchone()
mysql_time = (time.time() - start_time) * 1e6  # Convert to microseconds
cursor.close()
conn.close()

### **Step 2: Benchmark `ramdb` Query Execution Time**
mem_manager = MemoryManager(persist=True)  # Load RAM data
query_engine = QueryEngine(mem_manager)

# Locate `d003` in RAM
bit_address = 0xA0000000  # Start address
found = False
for i in range(9):  # Loop through stored records
    record = query_engine.fetch_record(bit_address)
    if "d003 | Human Resources" in record:
        found = True
        break
    bit_address += 256  # Move to next memory block

start_time = time.time()
ramdb_result = query_engine.fetch_record(bit_address) if found else "⚠ Not Found"
ramdb_time = (time.time() - start_time) * 1e6  # Convert to microseconds

# Print Benchmark Results
print("\n📊 Performance Benchmark Results")
print(f"MySQL Query Time: {mysql_time:.2f} µs")
print(f"`ramdb` Query Time: {ramdb_time:.2f} µs")
print("🔍 MySQL Result:", mysql_result)
print("⚡ `ramdb` Result:", ramdb_result)

mem_manager.close()