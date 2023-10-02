import heapq
from collections import defaultdict
from typing import List

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        tails = defaultdict(list)

        for n in nums:
            if tails[n - 1]:
                length = heapq.heappop(tails[n - 1]) + 1
                heapq.heappush(tails[n], length)
            else:
                heapq.heappush(tails[n], 1)

        for key in tails:
            if tails[key] and min(tails[key]) < 3:
                return False

        return True