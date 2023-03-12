class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        self.rowIndex=rowIndex
        result=self.pascal([1],0)
        return result
    def pascal(self,list1,index):
        if index==self.rowIndex:
            return list1 
        nums=[1]*(len(list1)+1)
        for i in range(len(list1)-1):
            nums[i+1]=list1[i]+list1[i+1]
        return self.pascal(nums,index+1)
        
            