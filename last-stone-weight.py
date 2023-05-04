class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]=stones[i]*-1
        heapq.heapify(stones)
        while len(stones)>1:
            first=-1*heapq.heappop(stones)
            second=-1*heapq.heappop(stones)
            result=abs(first)-abs(second)
            heapq.heappush(stones,-1*result)
        return stones[0]*-1