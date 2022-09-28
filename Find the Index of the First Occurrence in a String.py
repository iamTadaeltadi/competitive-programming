class Solution:
    def strStr(self, h: str, n: str) -> int:
        b=len(n)
        for i in range(len(h)-len(n)+1):
            if h[i:i+b]==n:
                return i
            
        return -1
            
