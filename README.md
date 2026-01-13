# Python Hash Table

This project implements a Hash Table data structure from scratch in Python. It handles data storage, retrieval, and collision management using a simple hashing algorithm (Sum of Unicode values).

## Features

* **Hash Function**: Converts string keys into integer indices based on ASCII values.
* **Collision Handling**: Uses nested dictionaries to store multiple keys that generate the same hash.
* **CRUD Operations**: Supports adding, looking up, and removing key-value pairs.

## Usage

1. **Run the script**:

   ```bash
   python main.py
   ```
2. **Class Methods**:

   * `hash(key)`: Returns the hash integer.
   * `add(key, value)`: Stores data.
   * `remove(key)`: Deletes data.
   * `lookup(key)`: Retrieves data (returns `None` if not found).

## License

This project is licensed under the [MIT License](LICENSE).
