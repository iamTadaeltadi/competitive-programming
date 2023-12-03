class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        

        return 0 if (max(nums)-k) - (min(nums)+k)<=-1 else (max(nums)-k) - (min(nums)+k)