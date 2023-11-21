class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={i:j for i,j in enumerate(nums)}
        def get_key(val):
            for key, value in d.items():
                if val == value:
                    return key
 
        print(d)
        for i,j in enumerate(nums):
            del d[i]
            if target-j in d.values():
                return [i,get_key(target-j)]
            d[i]=j
       
        
            
        
        
        
        