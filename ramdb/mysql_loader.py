import mysql.connector
from query_engine import QueryEngine

class MySQLLoader:
    def __init__(self, host, user, password, database, table):
        """Initialize MySQL connection."""
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()
        self.table = table

    def load_data_into_ramdb(self, query_engine):
        """Fetch data from MySQL and store in `ramdb`."""
        self.cursor.execute(f"SELECT dept_no, dept_name FROM {self.table}")
        records = self.cursor.fetchall()

        # Assign RAM bit addresses
        bit_offset = 0xA0000000  # Start address
        for record in records:
            record_data = f"{record[0]} | {record[1]}"  # Convert tuple to formatted string
            print(f"🔹 Storing in RAM: {record_data} at {hex(bit_offset)}")  # Debugging output
            query_engine.insert_record(bit_offset, record_data)
            bit_offset += 256  # Move to next RAM block

        print(f"✅ {len(records)} records loaded into `ramdb` from MySQL (Table: {self.table})")

    def close(self):
        """Close the database connection."""
        self.cursor.close()
        self.conn.close()
