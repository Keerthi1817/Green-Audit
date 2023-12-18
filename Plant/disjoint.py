class disjoint:
    def __init__(self, n):
        self.par = list(range(n+1))
        self.rank = [0]*(n+1)
        self.size = [1]*(n+1)

    def findpar(self, node):
        if node == self.par[node]:
            return node
        self.par[node] = self.findpar(self.par[node])
        return self.par[node]

    def ubysize(self, u, v):
        pu = self.findpar(u)
        pv = self.findpar(v)
        if self.size[pu] <= self.size[pv]:
            self.par[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.par[pv] = pu
            self.size[pu] += self.size[pv]
