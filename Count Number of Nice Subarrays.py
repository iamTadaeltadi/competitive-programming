class Solution:
    def numberOfSubarrays(self, nums, k):
        subarrayCount = 0
        i,j = 0,0
        queue = deque()
        while( j < len(nums) ):
            if(nums[j] % 2 != 0): queue.append(j)
            if(len(queue) > k):
                while(len(queue) > k):
                    if(nums[i] % 2 != 0): queue.popleft()
                    i += 1
            if(len(queue) == k): subarrayCount += queue[0] - i + 1
            j += 1
        return subarrayCount
