class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        
        prime = [True] * (n+1)
        prime[0], prime[1] = False, False
        
        for i in range(2, int(n**0.5)+1):
            if prime[i]:
                for j in range(i*i, n, i):
                    prime[j] = False
                    
        res = [i for i in range(2, n) if prime[i]]
        
        return len(res)