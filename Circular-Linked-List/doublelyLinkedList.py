class Node:
    def __init__(self, data):
        self.data = data
        self.nextPtr = None
        self.prevPtr = None

class DLList:
    def __init__(self):
        self.firstPtr = Node(63)
        self.firstPtr.nextPtr = self.firstPtr
        self.firstPtr.prevPtr = self.firstPtr
        self.size = 0
    
    def addFirst(self,data):
        newNode = Node(data)
        newNode.nextPtr = self.firstPtr.nextPtr
        newNode.prevPtr = self.firstPtr
        self.firstPtr.nextPtr.prevPtr = newNode
        self.firstPtr.nextPtr = newNode
        self.size += 1

    def addLast(self, data):
        newNode = Node(data)
        newNode.nextPtr = self.firstPtr
        newNode.prevPtr = self.firstPtr.prevPtr
        self.firstPtr.prevPtr.nextPtr = newNode
        self.firstPtr.prevPtr = newNode
        self.size += 1

    def removeLast(self):
        if self.size == 0:
            print("List is empty")
            return
        tempPtr = self.firstPtr.prevPtr
        self.firstPtr.prevPtr = tempPtr.prevPtr
        tempPtr.prevPtr.nextPtr = self.firstPtr
        tempPtr.prevPtr = None
        self.size -= 1
        return tempPtr.data

    def removeFirst(self):
        if self.size == 0:
            print("List is empty")
            return
        tempPtr = self.firstPtr.nextPtr
        self.firstPtr.nextPtr = tempPtr.nextPtr
        tempPtr.nextPtr.prevPtr = self.firstPtr
        tempPtr.prevPtr = None
        self.size -= 1
        return tempPtr.data
    
    def ToList(self):
        result = []
        current = self.firstPtr.nextPtr
        while current != self.firstPtr:  
            result.append(current.data)
            current = current.nextPtr
        print('None')
        return result
    
    def size(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0

