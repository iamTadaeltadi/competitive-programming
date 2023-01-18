class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr)<3:# if arr of length less than 3
            return False

        max_val=max(arr)
        max_indx=arr.index(max_val) #to check index of max value of array
        check=True #i use two variable to check if the both block should be excuted
        c=True
        for i in range(1,len(arr)):
            
            if i<=max_indx:
                c=False
                if arr[i]<=arr[i-1]:
                    return False
            else:
                check=False
                if arr[i]>=arr[i-1]:
                    return False
        if  c or check: #checking both block inside loop was excuted
            return False
        return True 
                
                    
            
                    
                