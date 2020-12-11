# ArrayStack

class ArrayStack:
    
    def __init__(self):
        
        # Initalize a list
        self.data = []
        
        # return the number of elements in the stack
    def __len__(self):
        return len(self.data)
    
        # chech if the stack is empty
    def is_empty(self):
        return len(self.data) == 0
    
        # add element to the top of the stack
    def push(self, e):
        self.data.append(e)
        
        # return but do not remove element at the top of the stack
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return(self.data[-1])
    
        # remove element from the stack
    def pop(self):
        if self.is_empty:
            raise Empty('Stack is empty')
        return(self.data.pop())
    
    
def main():
    myStack = ArrayStack()
    
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
    