class Node:
    def __init__(self, data):
        self.data = data
        self.nextPtr = None

class SLList:
    def __init__(self):
        self.firstPtr = Node(63)
        self.endPtr = None
        self.size = 0
    
    def addFirst(self, x):
        newNode = Node(x)
        newNode.nextPtr = self.firstPtr.nextPtr
        self.firstPtr.nextPtr = newNode
        if self.endPtr is None:
            self.endPtr = newNode
        self.size += 1
    
    def addLast(self, x):
        newNode = Node(x)
        if self.endPtr is None:
            self.firstPtr = newNode
            self.endPtr = newNode
        else:
            self.endPtr.nextPtr = newNode
            self.endPtr = newNode
        self.size += 1

    def getFirst(self):
        if self.firstPtr is not None:
            print(f'First: {self.firstPtr.data}')
        else:
            print('The list is empty')
            
    def size(self):
        return self.size    

    def printLinkedList(self):
        current = self.firstPtr
        while current:  
            print(current.data, end=' -> ')
            current = current.nextPtr
        print('None')