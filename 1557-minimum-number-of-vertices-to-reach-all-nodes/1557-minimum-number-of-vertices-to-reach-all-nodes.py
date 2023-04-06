class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        B = set(range(n))
        for x,y in edges:
            if y in B:
                B.remove(y)
        return list(B)