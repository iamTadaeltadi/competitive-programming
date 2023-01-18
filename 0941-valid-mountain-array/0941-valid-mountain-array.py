class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr)<3:
            return False

        max_val=max(arr)
        max_indx=arr.index(max_val)
        print(max_indx)
        check=True
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
        if  c or check:
            return False
        return True 
                
                    
            
                    
                