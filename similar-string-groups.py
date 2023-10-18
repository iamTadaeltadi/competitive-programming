class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = size
        self.rank = [1 for i in range(size)]

    def find(self, member):
        root = member

        while root != self.parent[root]:
            root = self.parent[root]

        while member != root:
            parent = self.parent[member]
            self.parent[member] = root
            member = parent
        return root

    def union(self, x, y):
        repx = self.find(x)
        repy = self.find(y)

        if repx != repy:
            if self.rank[repx] > self.rank[repy]:
                self.parent[repy] = repx
            elif self.rank[repx] < self.rank[repy]:
                self.parent[repx] = repy
            else:
                self.parent[repy] = repx
                self.rank[repx] += 1

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        n = len(strs)
        union = UnionFind(n)
        

        for i in range(len(strs)):
            for j in range(i+1,len(strs)):

                if union.find(i) == union.find(j):
                    continue

                diff = 0
                

                for k in range(len(strs[0])):
                    if strs[i][k] != strs[j][k]:
                        diff+=1

                        if diff>2:
                            break

                if diff<=2:
                    union.union(i,j)


        for i in range(n):
            union.find(i)
        return len(set(union.parent))