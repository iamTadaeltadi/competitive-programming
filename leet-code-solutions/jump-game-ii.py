class Solution:
    def jump(self, nums: List[int]) -> int:
        arr =[nums[0]]

        if len(nums)==1:
            return 0

        for i in range(1,len(nums)):
            arr.append(max(arr[-1]-1,nums[i]))
        print(arr)
        index =0
        count=0

        while index <len(arr)-1:
            print(index)
            count+=1
            index += arr[index]

        return count 
        


