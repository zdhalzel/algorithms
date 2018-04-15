"""A HashTable class inspired by Udacity that stores strings in a hash table,
where keys are calculated using the first two letters of the string."""


class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, key):
        value = [ord(i) for i in key]
        # the value is an array of ascii values of every letter in the string
        hash_value = self.calculate_hash_value(key)
        if self.table[hash_value] is None:
            self.table[hash_value] = [(key,value)]
        else:
            self.table[hash_value].append((key,value))

    def lookup(self, key): # returns the hash_value if the key is in the table
        hash_value = self.calculate_hash_value(key)
        if self.table[hash_value] is not None:
            if key in dict(self.table[hash_value]):
            # for tuple in self.table[hash_value]:
                # if tuple[0] is key:
                    return hash_value
        return -1

    def calculate_hash_value(self, key):
        return (ord(key[0]) * 100) + ord(key[1])

# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print
hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
# Should be -1
print
hash_table.lookup('UDACITY')

# Test store
hash_table.store('UDACITY')
# Should be 8568
print
hash_table.lookup('UDACITY')

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print
hash_table.lookup('UDACIOUS')
