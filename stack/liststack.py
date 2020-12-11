# ListStack

'''
Implementing the list Stack works like the array stack, except that the methods of a Python
list are not used and nodes are created and linked when adding to the stack

For this implementation, we will create 2 classes; a node class and the stack methods.

This is unlike the array stack method which had an apmty list and the stack methods

'''

class ListStack:
    
    # --------------------- Node Class -------------
    class Node:
        
        # streamlines memory usage
        __slots__ = 'element', 'next'
        
        # initializes the node fields
        def __init__(self, element, next):
            self.element = element
            self.next = next
            
    
    # --------------------- Stack Methods -------------
    def __init__(self):
        
        # creates an empty stack
        self.head = None
        self.size = 0
        
        
        # return the number of elements in the stack
    def __len__(self):
        return self.size
    
    
        # chech if the stack is empty
    def is_empty(self):
        return self.size == 0
    
    
        # add element, e to the top of the stack
    def push(self, e):
        # create a new node e, add it to the head of the stack and link the new node to the existing
        # head element.
        self.head = self.Node(e, self.head)
        
        
        # return but do not remove element at the top of the stack
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.head.element
    
    
        # remove element from the stack
    def pop(self):
        if self.is_empty:
            raise Empty('Stack is empty')
        answer = self.head.element
        self.head = self.head.next
        self.size -= 1
        return answer
    
    
def main():
    myStack = ListStack()
    
    myStack.push(2)
    myStack.push(4)
    myStack.push(6)
    myStack.push(8)
    myStack.push(11)
    myStack.push(44)
    
    print('The number of elements in the stack is {}'.format(myStack.__len__()))
    print('The stack is empty? {}'.format(myStack.is_empty()))
    print('The first element in the stack is {}'.format(myStack.top()))
    
main()
    