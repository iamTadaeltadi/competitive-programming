class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def solve(start, end):
            prime = [True for i in range(end + 1)] # initially mark all numbers as prime
            p = 2
            
            while(p * p <= end):
                if prime[p]:
                    for i in range(p * p, end + 1, p):
                        prime[i] = False # mark all multiples except for the first number as non-prime
                p += 1
            
            res = deque()
            ans = []
            
            for p in range(max(2, start), end + 1):
                if prime[p]:
                    res.append(p)
                    if len(res) == 2:
                        ans.append((res[1] - res[0],  res[0], res[1]))
                        res.popleft()
            print(ans)
            ans.sort()
            return (ans[0][1],ans[0][2]) if ans else [-1, -1]
        
        return solve(left, right)