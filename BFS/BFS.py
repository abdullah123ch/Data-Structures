class BFS:
    def bfs(self, Adj, s):
        parent = [None for v in Adj]
        parent[s] = s
        level = [[s]]                   # level[0] contains the start node
        while 0 < len(level[-1]):
            level.append([])            # create the next level
            for u in level[-2]:         # loop over nodes in previous level
                for v in Adj[u]:        # check neighbors
                    if parent[v] is None:
                        parent[v] = u
                        level[-1].append(v)
        return parent

    def unweighted_shortest_path(self, Adj, s, t):
        parent = self.bfs(Adj, s)       # O(V + E) BFS tree from s
        if parent[t] is None:           # O(1) t reachable from s?
            return None                 # O(1) no path
        i = t                           # O(1) label of current vertex
        path = [t]                      # O(1) initialize path
        while i != s:                   # O(V) walk back to s
            i = parent[i]               # O(1) move to parent
            path.append(i)              # O(1) amortized add to path
        return path[::-1]

