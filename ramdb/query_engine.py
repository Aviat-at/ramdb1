from memory_manager import MemoryManager

class QueryEngine:
    def __init__(self, memory_manager):
        self.memory_manager = memory_manager

    def insert_record(self, bit_address, record):
        """Insert a record into RAM at the given bit-address."""
        formatted_record = record.strip()  # Ensure no trailing spaces
        memory_offset = bit_address - 0xA0000000  # Calculate offset
        print(f"📝 Inserting Record: '{formatted_record}' at {hex(bit_address)} (Offset: {memory_offset})")
        self.memory_manager.allocate_memory(formatted_record, memory_offset)

    def fetch_record(self, bit_address):
        """Retrieve a record using bit-address lookup."""
        memory_offset = bit_address - 0xA0000000  # Calculate offset
        record = self.memory_manager.fetch_memory(memory_offset)  # Correct method call
        print(f"🔍 Fetching Record at {hex(bit_address)} (Offset: {memory_offset}): '{record}'")
        return record if record else "⚠ No Data Found"
