class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        if row == 0:
            return []
        col = len(matrix[0])
        l = 0
        r = col - 1
        a = 0
        b = row - 1
        ans = []
        while r >= l and b >= a:
            for i in range(l, r + 1):
                ans.append(matrix[a][i])
            a += 1
            for i in range(a, b + 1):
                ans.append(matrix[i][r])
            r -= 1
            if a <= b:
                for i in range(r, l - 1, -1):
                    ans.append(matrix[b][i])
                b -= 1
            if l <= r:
                for i in range(b, a - 1, -1):
                    ans.append(matrix[i][l])
                l += 1
        return ans
