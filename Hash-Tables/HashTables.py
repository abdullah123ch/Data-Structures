class Vertix:
    def __init__(self, n, c):
        self.n = n
        self.c = c
        self.next = None

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity
        self.size = 0
        self.FirstPtr = None

    def hash_function(self, n ,c):
        hash = str(n) + str(c)
        hashcode = 0
        for i in hash:
            hashcode += ord(i)
        index = hashcode % self.capacity
        return index

    def insert(self, n, c):
        index = self.hash_function(n, c)
        newNode = Vertix(n, c)
        if (self.size / self.capacity) >= 0.75:
            self.resize()
        if self.table[index] is None:
            self.table[index] = newNode    
        else:
            self.FirstPtr = self.table[index]
            self.table[index] = newNode
            newNode.next = self.FirstPtr
            self.FirstPtr = None
        self.size += 1  

    def resize(self):
        new_capacity = self.capacity * 2
        new_table = [None] * new_capacity
        for i in range(self.capacity):
            current = self.table[i]
            while current:
                index = self.hash_function(current.n, current.c) % new_capacity
                new_node = Vertix(current.n, current.c)
                new_node.next = new_table[index]
                new_table[index] = new_node
                current = current.next
        self.table = new_table
        self.capacity = new_capacity

    def contains(self, n ,c):
        index = self.hash_function(n, c)
        current = self.table[index]
        while current:
            if current.n == n and current.c == c:
                return True
            current = current.next
        return False

    def display(self):
        for i in range(self.capacity):
            print(f"Index {i}:", end=" ")
            temp = self.table[i]
            while temp:
                print(f"({temp.n}, {temp.c})", end=" -> ")
                temp = temp.next
            print("None")
        
    
