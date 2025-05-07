class DFS:
    def dfs(self,Adj, s, parent=None, order=None):
        if parent is None:
            parent = [None for v in Adj]
            parent[s] = s
            order = []
        for v in Adj[s]:
            if parent[v] is None:
                parent[v] = s
                self.dfs(Adj, v, parent, order)
        
        order.append(s)
        return parent, order

