class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sett=set()
        def recur(arr,index):
            curr=arr.copy()
            if len(arr)>=2 and arr[-1] >=arr[-2] and tuple(curr) not in sett:
                res.append(curr)
                sett.add(tuple(curr))
            if len(arr)>=2 and arr[-1] <arr[-2]:
                return 

                
            for i in range(index,len(nums)):
                arr.append(nums[i])
                recur(arr,i+1)
                arr.pop()
        recur([],0)
        return res
