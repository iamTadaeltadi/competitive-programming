class Solution:
    def splitString(self, s: str) -> bool:
        res=[]
        
        
        def splitter(index,res):
            if index==len(s) - 1:
                return False
            res.append(int(s[:index + 1]))
            val=s[index+1:]
            
            string=""
            for i in val:
                string+=i
                if  ( res[0]!=0 and (res[-1]==0) and int(string)==0) or res[-1]- int(string)==1:
                    
                    res.append(int(string))
                    string=''
                    
            if not string:
                return True
            else:
                return splitter(index+1,[])
        ress = splitter(0,[])
        return ress
        
            
            
            
            