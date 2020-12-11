import ctypes

class Arrays:
    
    def __init__(self):
        self._n = 0     #Count of elements in the array
        self._capacity = 1      #Array capacity, default is 1
        self._A = self._make_array(self._capacity)      #The actual array we are working with
        
    
    #  Method to get an item form an array
    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]
    
    
    # Method to add object to an array
    def __append__(self, obj):
        if self._n == self._capacity:   #If the number of elements is equalt to capacity (if the array is full)
            
            # Increase size of the array
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        
        # Increase the n variable (no of elements in the array) by 1)
        self._n += 1
     
     
    # Method to resize existing array   
    def _resize(self, c):
        
        B = self._make_array(c)     # Create a bigger array
        
        # For each element self._n in the Array, self._A, assign every element in A to every cell in B
        for  k in range(self._n):
            B[k] = self._A[k] 
              
        self._A = B     # Re-assign A to B
        self._capacity = c      # Re-assign the capacity of A tot he capapity, c of B
    
    
    # Method to return length of the array
    def __len__(self):
        return self._n
     

    
    # Method to create an array
    def _make_array(self, c):
        return (c * ctypes.py_object)()
        
    
    
d = Arrays()

print(len(d))