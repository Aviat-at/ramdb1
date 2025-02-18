# ramdb

ramdb is a lightweight, in-memory database built using Python's memory-mapped file capabilities. It simulates a simple database system by loading data (e.g., from MySQL) into RAM, enabling rapid query responses and benchmarking comparisons between traditional MySQL queries and in-memory queries.

## Features

- **In-Memory Data Storage:** Utilizes a memory-mapped file to simulate a RAM database.
- **MySQL Integration:** Load data directly from MySQL tables (e.g., the departments table from an employees database) into RAM.
- **Fast Query Execution:** Offers a query engine that performs bit-address based lookups for fast data retrieval.
- **Performance Benchmarking:** Compare query execution times between MySQL and ramdb.
- **Debug and Testing Tools:** Includes scripts for testing MySQL connections, loading data, and debugging RAM storage.
- **Swap System:** Contains a simple mechanism to move data from RAM to disk (SSD) when memory is limited.

## File Overview

- **benchmark_ram_vs_mysql.py:** Benchmarks and compares the query performance of MySQL versus the in-memory ramdb.
- **test_mysql_loader.py:** Loads the departments table from MySQL into ramdb and prints all stored records for verification.
- **query_engine.py:** Provides methods for inserting and fetching records using bit-address lookup.
- **memory_manager.py:** Manages the low-level memory mapping, including allocation and fetching of records.
- **debug_ram_storage.py:** Debug utility that reloads data into ramdb and prints stored records for troubleshooting.
- **mysql_loader.py:** Connects to a MySQL database and loads selected table data into the in-memory ramdb.
- **test_mysql_connection.py:** Verifies the connection to the MySQL database and lists available tables.
- **swap_system.py:** Implements a basic swap mechanism to offload records from RAM to disk when needed.

## Installation

### Prerequisites

- Python 3.6 or higher
- MySQL Server

### Python Packages

- `mysql-connector-python`

### Setup Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Aviat-at/ramdb.git
   cd ramdb
