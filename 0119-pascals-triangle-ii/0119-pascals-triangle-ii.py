class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def rec(index, list1):
            if index == rowIndex:
                return list1
            n = len(list1)
            q = [1]*(n + 1)
            for i in range(n - 1):
                q[i + 1] = list1[i] + list1[i+1]
            return rec(index + 1, q)
        return rec(0, [1])
                
        