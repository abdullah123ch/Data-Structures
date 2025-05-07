class Graph:
    def __init__(self, vertices):
        self.edges = 0
        self.L = [[] for _ in range(vertices)]

    def add_edge(self, v, w): 
        self.L[v].append(w)
        self.L[w].append(v)
        self.edges += 1

    def vertices(self):
        return len(self.L)
    
    def edges(self):
        return self.edges
    
    def degree(self, v):
        return len(self.L[v])
    
    def display(self):
        for v in range(len(self.L)):
            print(f"{v}: {', '.join(map(str, self.L[v]))}")           

data = {
    0: "action",
    1: "change",
    2: "demotion",
    3: "descent",
    4: "jump parachuting",
    5: "increase",
    6: "jump leap",
    7: "augmentation",
    8: "antihistamine",
    9: "nasal_decongestant",
    10: "actifed"
}
g = Graph(11) 
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(3, 4)
g.add_edge(5, 6)
g.add_edge(5, 7)
g.add_edge(8, 10)
g.add_edge(9, 10)
g.display()