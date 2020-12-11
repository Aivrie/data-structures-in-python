# DOUBLY LINKED LISTS

'''
Each node of a linked list is represented as a unique object with that instance
storing;
1.) A reference to its element (data)
2.) A reference to the next node (or None for the tail)(pointer)

A second object represents the linked list as a whole

To begin implementing, you Must create a HEAD node and you should create a TAIL node
and a get_size method to keep count of the number of nodes in the list

'''

# NODE CLASS

class Node:
    
        # constructor
    def __init__(self, data, n=None, p=None):
        self.data = data
        self.next_node = n
        self.prev_node = p
        
        # Method to get the next node
    def get_next(self):
        return self.next_node
    
        # Method to set the next node (takes an argument, n)
    def set_next(self, n):
        self.next_node = n
        
        # Method to get the prev node
    def get_prev(self):
        return self.prev_node
    
        # Method to set the prev node (takes an argument, n)
    def set_prev(self, p):
        self.prev_node = p
    
        # Method to get data from the list
    def get_data(self):
        return self.data
    
        # Methodto set data to the list
    def set_data(self, data):
        self.data = data
    
    
class LinkedList:
    
        # constructor
    def __init__(self, r = None):
        self.root = r
        self.size = 0
        
        
        # Get the number of nodes in the linkedlist (size of the linked list)
    def get_size(self):
        return self.size
    
    
        # Create a new node with passed in data and add node to list
    def add(self, data):
        
        # create new node using the Node class above
        new_node = Node(data, self.root)
        
        # if there is already a node in the list, set the prev of root node to new node
        if self.root:
            self.root.set_prev(new_node)
            
        # set new node to root
        self.root = new_node
        # increase size by 1 on addition of the new node
        self.size += 1
        
        
        # delete a node form the list
    def remove(self, d):
        
        # Head node
        current_node = self.root
        
        while current_node is not None:
            # if the current node has our target data
            if current_node.get_data() == d:
                # get the next and prev values of the target node
                next = current_node.get_next()
                prev = current_node.get_prev()
                    
                # if next is not None
                if next:
                # set (point) the next value of the current node to its prev value
                    next.set_prev(prev)
                # if prev is not None
                if prev:
                # set (point) the prev value of the current node to its next value
                    prev.set_next(next)
                    
                # if root node is the target node, set the root node to the next node
                else:
                    self.root = current_node
                    
                self.size -= 1
                return True
            
            else:
                current_node = current_node.get_next()
        return False
        
        
        # find target data in the list
    def find(self, d):
        current_node = self.root
        while current_node is not None:
            if current_node.get_data == d:
                return d
            elif current_node.get_next() == None:
                return False
            else:
                current_node = current_node.get_next()
    
def main():
    myList = LinkedList()
    myList.add(2)
    myList.add(4)
    myList.add(6)
    myList.add(8)
    myList.add(10)
    myList.add(13)
    myList.add(24)
    
    print('Size of the list is {}'.format(myList.get_size()))
    # print(type(myList))
    print(myList.get_size())
    print(myList.find(12))
    print(myList.remove(10))
    print(myList.get_size())

main()
