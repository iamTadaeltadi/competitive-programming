n=int(input())
for i in range(n):
    x=int(input())
    index=0
    ans=0
    while x>0:
        if x&1==1:
            ans+=2**index
            x>>=1
            break
        x>>=1
        index+=1
    if x==0 and index==0:
        ans+=2
    elif x==0 :
        ans+=1
    print(ans
