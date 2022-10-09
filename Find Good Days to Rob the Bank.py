class Solution:
        def goodDaysToRobBank(self, A: List[int], t: int) -> List[int]:
            if t == 0: return list(range(len(A)))
            lft, rgt, n = [0], [0], len(A)

            # Build non-increasing on the left side (inclusive).
            curr = 0
            for i in range(1, n):
                if A[i] <= A[i - 1]:
                    curr += 1
                else: 
                    curr = 0
                lft.append(curr)
            print(lft)

            # Build non-decreasing on the right side (inclusive).
            curr = 0
            for i in range(n - 2, -1, -1):
                if A[i] <= A[i + 1]: curr += 1
                else: curr = 0
                rgt.append(curr)
            rgt.reverse()
            print(rgt)
            y=[]
            for i in range(n):
                if lft[i] >= t  and rgt[i] >= t :
                    y.append(i)
            return y
