# Hashtable implementation

# Step 1: Generate your hash function
def hash_func(key):
    h = 0
    for char in key:
        h += ord(char)
    return h % 10

# No Collision Handling

# class Hashtable:
#     def __init__(self):
#         self.MAX = 10
#         self.arr = [None for i in range(self.MAX)]
        
#     def hash_func(self, key):
#         h = 0
#         for char in key:
#             h += ord(char)
#         return h % 10
    
#     # inserting data into the hash table (M[k] = v)
#     def __setitem__(self, key, val):
#         h = self.hash_func(key)
#         self.arr[h] = val
        
#     def __getitem__(self, key):
#         h = self.hash_func(key)
#         return self.arr[h]
    
#     def __delitem__(self, key):
#         h = self.hash_func(key)
#         self.arr[h] = None



# Collision Handling

class Hashtable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        
    def hash_func(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 10
    
    
    # inserting data into the hash table (M[k] = v)
    def __setitem__(self, key, val):
        h = self.hash_func(key)
        
        found = False
        # if element exists in hashmap
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break
        # if element doesn't exist in hashmap
        if not found:
        # Append key-value pair to the list at key, h
            self.arr[h].append((key, val))
        
    
    # getting data from the hash table (M[k])
    def __getitem__(self, key):
        h = self.hash_func(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
 
    
    # deleting data from the hash table (del M[k])
    def __delitem__(self, key):
        h = self.hash_func(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]


m = Hashtable()
m['ivory'] = 10
m['sandy'] = 1050
m['Jackie'] = 107
m['Paul'] = 67
# print(m.arr)
# print(m['ivory'])
print(m.arr)
