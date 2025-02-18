import pickle

class SwapSystem:
    def __init__(self, swap_file="swap.db"):
        self.swap_file = swap_file

    def save_to_swap(self, bit_address, record):
        """Move old records from RAM to SSD when RAM is full."""
        with open(self.swap_file, "ab") as f:
            pickle.dump({bit_address: record}, f)

    def fetch_from_swap(self, bit_address):
        """Retrieve records from SSD when needed."""
        try:
            with open(self.swap_file, "rb") as f:
                while True:
                    try:
                        data = pickle.load(f)
                        if bit_address in data:
                            return data[bit_address]
                    except EOFError:
                        break
        except FileNotFoundError:
            return None
