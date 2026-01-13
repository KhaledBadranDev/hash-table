class HashTable:
    def __init__(self):
        """
        Initialize the hash table.
        The collection attribute holds the data.
        It is a dictionary where keys are hash integers and values are nested dictionaries.
        """
        self.collection = {}

    def hash(self, key):
        """
        Compute the hash value for a given string key.
        It sums the Unicode (ASCII) values of each character in the string.
        """
        total = 0
        for char in key:
            total += ord(char)
        return total

    def add(self, key, value):
        """
        Add a key-value pair to the hash table.
        It handles collisions by storing multiple keys in a nested dictionary
        under the same hash index.
        """
        hashed_key = self.hash(key)
        
        # If the hash index does not exist, create a new dictionary for it
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}
            
        # Add or update the key-value pair in the nested dictionary
        self.collection[hashed_key][key] = value

    def remove(self, key):
        """
        Remove a key-value pair from the hash table.
        If the key does not exist, it does nothing.
        """
        hashed_key = self.hash(key)
        
        # Check if the hash bucket exists
        if hashed_key in self.collection:
            # Check if the specific key exists in that bucket
            if key in self.collection[hashed_key]:
                del self.collection[hashed_key][key]

    def lookup(self, key):
        """
        Retrieve a value by its key.
        Returns None if the key is not found.
        """
        hashed_key = self.hash(key)
        
        # Check if the hash bucket exists and contains the key
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            return self.collection[hashed_key][key]
        
        return None

# --- Manual Testing Block ---
if __name__ == "__main__":
    # Create instance
    ht = HashTable()

    # Test 1: Hash calculation
    # 'golf' -> g(103) + o(111) + l(108) + f(102) = 424
    print(f"Hash for 'golf': {ht.hash('golf')}") 

    # Test 2: Add simple item
    ht.add('golf', 'sport')
    print(f"Lookup 'golf': {ht.lookup('golf')}")

    # Test 3: Add collision items ('dear' and 'read' both sum to 412)
    ht.add('dear', 'friend')
    ht.add('read', 'book')
    
    # Verify collision storage structure
    # Should show dictionary at key 412 containing both items
    print(f"Collection at 412: {ht.collection.get(412)}")

    # Test 4: Lookup inside collision
    print(f"Lookup 'read': {ht.lookup('read')}")

    # Test 5: Remove item
    ht.remove('dear')
    print(f"Collection at 412 after removing 'dear': {ht.collection.get(412)}")
    
    # Test 6: Lookup removed item
    print(f"Lookup 'dear': {ht.lookup('dear')}")

    # Test 7: Output format check for 'rose'
    ht.add('rose', 'flower')
    # 'rose' -> 114 + 111 + 115 + 101 = 441
    print(f"Collection structure for rose: {{ 441: {ht.collection[441]} }}")