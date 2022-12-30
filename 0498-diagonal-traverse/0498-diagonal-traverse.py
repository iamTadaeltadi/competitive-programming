class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]     
        :rtype: List[int]
        """
        rows=len(mat)
        columns=len(mat[0])
        tot=rows+columns-1
        r=0
        t=True
        res=[]
        cur=[[]]*tot
        ii=1
        for i in range(tot):
            cur=[]
          
            if i<=columns-1:
                c=0
            else:
                i=columns-1
                if t:
                    c=1
                else:
                    c+=1
                t=False
            r=c    
            while i>=0 and r<rows:
                cur.append(mat[r][i])
                r+=1
                i-=1
            if ii%2==1:
                res.append(cur[::-1])
            else:
                res.append(cur)
            ii+=1
        li = list([i for j in res for i in j])
        return li
    
    

                
        
        