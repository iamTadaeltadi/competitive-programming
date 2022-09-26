  l,r=0,0 
        x=[]
        z=[]
        while l<len(s):
            if s[l] in s[r:]:
                x.append(s[r])
                r+=1
            else:
                s[l] not in s[r:]
                l+=1
            
            if l==r:
                z.append(len(x))
                x=[] 
            
        return z
            
