class PQ:
    def __init__(self):
        self.L = []
        self.size = 0

    def getParentOf(self, i):
        return (i - 1) // 2

    def getLeftOf(self, i):
        return 2 * i + 1

    def getRightOf(self, i):
        return 2 * i + 2

    def min(self, i1, i2):
        if i1 >= self.size:  # If i1 is out of bounds, return i2
            return i2
        if i2 >= self.size:  # If i2 is out of bounds, return i1
            return i1
        return i1 if self.L[i1] < self.L[i2] else i2

    def swimUp(self):
        i = self.size - 1
        while i > 0:
            parent = self.getParentOf(i)
            if self.L[i] < self.L[parent]:
                self.L[i], self.L[parent] = self.L[parent], self.L[i]
                i = parent
            else:
                break

    def swimDown(self, i):
        while True:
            left = self.getLeftOf(i)
            right = self.getRightOf(i)
            smallest = self.min(left, right)
            if smallest < self.size and self.L[smallest] < self.L[i]:
                self.L[i], self.L[smallest] = self.L[smallest], self.L[i]
                i = smallest
            else:
                break

    def insert(self, item):
        self.L.append(item)
        self.size += 1
        self.swimUp()

    def peek(self):
        if self.size == 0:
            return None
        return self.L[0]

    def poll(self):
        if self.size == 0:
            return None  
        root = self.L[0]  
        self.L[0] = self.L[self.size - 1]  
        self.L.pop()  
        self.size -= 1
        if self.size > 0:
            self.swimDown(0)  
        return root