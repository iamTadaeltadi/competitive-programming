n,m=map(int,input().split(" "))
nums=list(map(int,list(input().split(" "))))
nums2=list(map(int,list(input().split(" "))))
l=0
answer=[]
for i in range(m):
    while l<n and nums[l] <nums2[i]:
        l+=1
    answer.append(l)
print(*answer)
