class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
       
        if n <=0:
            return False

        def recur(n):
            if n == 1 :
                return True
            if n % 2 != 0:
                return False
            return recur(n // 2)

        return recur(n)