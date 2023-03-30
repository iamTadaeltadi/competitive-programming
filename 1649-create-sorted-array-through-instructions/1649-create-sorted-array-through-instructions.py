class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        
        self.instructions=instructions
        merged=self.mergesort(0,len(instructions)-1)
        tot=0
        # print(merged)
        for i in merged:
            tot+=min(i[1],i[2])
        return (tot)%(10**9+7)
    def mergesort(self,left,right):
        if left==right:
            return [[self.instructions[left],0,0]]
        mid=(left)+(right-left)//2
        
        left=self.mergesort(left,mid)
        right=self.mergesort(mid+1,right)
        n,m=len(left),len(right)
       
        left_val=[ i[0] for i in left]
        for i in range(m):
            bisect_l=bisect.bisect_left(left_val,right[i][0])
            bisect_r=bisect.bisect_right(left_val,right[i][0])
            right[i][1]+=n-bisect_r
            right[i][2]+=bisect_l
        left = left + right
        left.sort()
        return left
        # return self.merge(left,right)
    # def merge(self,left,right):
    #     result=[]
    #     l=0
    #     r=0
    #     n,m=len(left),len(right)
    #     while l<n and r<m:
    #         if left[l][0]<right[r][0]:
    #             result.append(left[l])
    #             l+=1
    #         else:
    #             result.append(right[r])
    #             r+=1
    #     while l<n:
    #         result.append(left[l])
    #         l+=1
    #     while r<m:
    #         result.append(right[r])
    #         r+=1
    #     return (result)
    
            
            
        
        