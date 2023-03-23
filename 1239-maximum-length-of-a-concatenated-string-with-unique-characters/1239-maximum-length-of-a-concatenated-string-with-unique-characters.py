class Solution:
    def maxLength(self, arr) -> int:
        def isUniqueChars(string):
            freq = Counter(string)
            
            if(len(freq) == len(string)):
                return True
            else:
                return False
        res=0
        
        def cocatnate(index,curr):
            cocatnatedStr="".join(curr)
            
            nonlocal res
            
            if not isUniqueChars(cocatnatedStr):
                return 
            print(cocatnatedStr,curr)
            res=max(len(cocatnatedStr),res)
            if res==len("".join(arr)):
                return 
            
            for i in range(index,len(arr)):
                curr.append(arr[i])
                cocatnate(i+1,curr)
                curr.pop()
            
        cocatnate(0,[])
        return res
            
            
        
