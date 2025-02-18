import mmap
import os

class MemoryManager:
    def __init__(self, mem_size=1024 * 1024, persist=False):
        """Initialize RAM storage with optional persistence."""
        self.mem_size = mem_size
        self.mem_file = "/tmp/ramdb"
        self.persist = persist

        if self.persist and os.path.exists(self.mem_file):
            print("🔄 Loading existing RAM data from disk...")
        else:
            print("🆕 Creating new RAM storage...")

        # Ensure file size matches `mem_size`
        with open(self.mem_file, "a+b") as f:
            f.truncate(self.mem_size)  # **Guarantees the file is exactly `mem_size` bytes**

        # Open the file for reading/writing
        self.fd = os.open(self.mem_file, os.O_RDWR)
        self.memory_map = mmap.mmap(self.fd, mem_size)

    def allocate_memory(self, data, offset):
        """Store data in RAM at a specific memory offset."""
        if offset < 0 or offset >= self.mem_size:
            raise ValueError(f"Invalid memory offset: {offset}")
        if len(data) > 64:  # Limit record size
            raise ValueError("Data size exceeds 64 bytes")

        print(f"💾 Storing Data at Offset: {offset} -> {data}")
        self.memory_map.seek(offset)
        self.memory_map.write(data.encode())  # Write data
        self.memory_map.flush()  # Ensure data is written to disk

    def fetch_memory(self, offset, size=64):
        """Retrieve data from RAM at a specific memory offset."""
        if offset < 0 or offset >= self.mem_size:
            return "⚠ Invalid Memory Access"

        self.memory_map.seek(offset)  # Move to memory location
        data = self.memory_map.read(size).decode().strip()
        print(f"🔍 Reading Data at Offset: {offset} -> {data}")
        return data

    def close(self):
        """Close the memory-mapped file and persist data if needed."""
        print("📁 Closing MemoryManager and persisting data...")
        self.memory_map.flush()  # Ensure changes are saved
        self.memory_map.close()
        os.close(self.fd)  # Close file descriptor
