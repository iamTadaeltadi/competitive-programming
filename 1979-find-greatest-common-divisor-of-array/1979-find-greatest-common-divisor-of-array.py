class Solution:
    def findGCD(self, nums: List[int]) -> int:
        max_val=max(nums)
        min_val=min(nums)
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
        return gcd(max_val,min_val)