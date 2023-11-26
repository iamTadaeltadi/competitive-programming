class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        

        pairs = set()
        elm = set()
        count = 0
        
        for i in nums:
           
            if i +k in elm :
               if (i+k,i ) not in pairs and (i,i +k) not in pairs :
                   pairs.add((i,i+k))
                   count +=1
            if i -k in elm:
                if (i-k,i ) not in pairs and (i,i -k) not in pairs :
                   pairs.add((i,i-k))
                   count +=1
            elm.add(i)
        return count
            
        


