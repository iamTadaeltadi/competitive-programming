class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        arr.sort()
        x=1
        arr[0]=1
        for i in range(1,len(arr)):
            if abs(arr[i]-x)>1:
                arr[i]=x+1
                x+=1
            else:
                x=arr[i]


        return x