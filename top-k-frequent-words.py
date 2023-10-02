from heapq import *
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ump={}
        res = []
        for i in words:
            ump[i] = ump.get(i , 0) + 1

        maxheap = []
        for key , val in ump.items():
            heappush(maxheap , [-val , key])
        for _ in range(k):
            val , key = heappop(maxheap)
            res.append(key)

        #res.sort()
        return res