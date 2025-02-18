from memory_manager import MemoryManager
from query_engine import QueryEngine
from mysql_loader import MySQLLoader

# Initialize `ramdb`
mem_manager = MemoryManager()
query_engine = QueryEngine(mem_manager)

# Load `departments` table into `ramdb`
mysql_loader = MySQLLoader(
    host="localhost",
    user="root",
    password="akash123456",  # Change this!
    database="employees",
    table="departments"
)
mysql_loader.load_data_into_ramdb(query_engine)

# Debug: Print all stored records in RAM
print("\n📂 Checking stored records in RAM...")
bit_address = 0xA0000000
for i in range(9):  # Only check stored records
    stored_data = query_engine.fetch_record(bit_address)
    print(f"📝 Record at {hex(bit_address)}: {stored_data}")
    bit_address += 256  # Move to next memory block

# Cleanup
mysql_loader.close()
mem_manager.close()
