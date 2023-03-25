class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.res=[]
        for i in range(len(nums)):
            self.res.append([nums[i],i,0])
        self.mergesort(0,len(nums)-1)
        ans=[]
        for i in self.res:
            ans.append(i[2])
        return ans
            

        return self.res
    def mergesort(self,l,r):
        if l==r:
            return [self.res[l]]

        mid=(l+r)//2
        left=self.mergesort(l,mid)
        right=self.mergesort(mid+1,r)

        self.compare(left,right)
        return self.merge(left,right)
    def merge(self,left,right):
        
        l,r=0,0
        result=[]
        while l<len(left) and r<len(right):
            if left[l][0]<right[r][0]:
                result.append(left[l])
                l+=1
            else:
                result.append(right[r])
                r+=1
        while l<len(left):
            result.append(left[l])
            l+=1
        while r<len(right):
            result.append(right[r])
            r+=1
                
            
        return result
    def compare(self,left,right):
        
        # print(self.res)
        l=0
        for i in range(len(left)):
            while l<len(right) and left[i][0]>right[l][0]:
                l+=1
            
            self.res[left[i][1]][2]+=l
            
    
            
                


            