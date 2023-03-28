num=int(input())
for i in range(num):
    n,m=list(map(int,input().split()))
    coll=[0 for i in range(m+n-1)]
    roww=[0 for i in range(m+n-1)]
    tot=0
    matrix=[]
    for i in range(n):
        row=list(map(int,input().split()))
        matrix.append(row)
        for j in range(m):
           
            roww[n-1+j-i]+=(row[j])
            coll[j+i]+=(row[j])
            
    for i in range(n):
        for j in range(m):
            
            tot=max(tot,roww[n-1+j-i]+coll[j+i]-matrix[i][j])
    print(tot)
        
    
            
            
