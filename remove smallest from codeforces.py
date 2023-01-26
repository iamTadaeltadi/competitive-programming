n=int(input())
for i in range(n):
    m=int(input())
    strr=list(map(int,input().split()))
    strr.sort()
    res=""
    if m==1:
        print("YES")
        continue
    for i in range(1,m):
        if strr[i]-strr[i-1]>1:
            res="NO"
            break
        else:
            res="YES"
    print(res)
            
            
    
    
