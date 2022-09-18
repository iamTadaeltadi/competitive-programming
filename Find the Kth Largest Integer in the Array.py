class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        n=list(map(int,nums))
        n.sort()
        c=list(map(str,n[::-1]))
        return c[k-1]
            
