class AList:
    def __init__(self):
        self.items = [0] * 10
        self.capacity = len(self.items)
        self.Currentsize = 0

    def addLast(self,i):
        if self.Currentsize == self.capacity:
            self.resize(2 * self.capacity)
        self.items[self.Currentsize] = i 
        self.Currentsize += 1
    
    def removeLast(self):
        if self.size == 0:
            raise IndexError("The list is empty")
        if (self.Currentsize/self.capacity) < (1/4):
            self.resize(self.capacity // 2)
        self.Currentsize -= 1
        print("the last item removed is",self.items[self.Currentsize])
        self.items[self.Currentsize] = 0

    def getLast(self):
        print(self.items[self.Currentsize - 1])
        return
    
    def get(self,i):
        if i < 0 or i >= self.Currentsize:
            return None
        print(self.items[i])
        return

    def size(self):
        print(f'size = {self.Currentsize} \n capacity = {self.capacity}')
        return
    
    def resize(self, i):
        newArray = [0] * i
        for j in range(self.Currentsize):
            newArray[j] = self.items[j]
        self.items = newArray
        self.capacity = i
    
    def printList(self):
        print(self.items)

