#Masha and a Beautiful Tree the quetion on codeforces
n=int(input())
for i in range(n):
    m=int(input())
    arr=list(map(int,input().split()))
    res=[0]
    def mergeSort(left,right):
   
        if right==left:
            return [arr[left]]
        mid=left+(right-left)//2
        left=mergeSort(left,mid)
        right=mergeSort(mid+1,right)
        result = []
        l, r = 0, 0
        
        if left==None or right==None:
            res[-1]=-1
            return 
        while  l < len(left) and r < len(right):
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1

        result += left[l:]
        result += right[r:]
        if result==left+right:
            return result

        elif result==right+left:
            res[-1]+=1
            return result
        else:
            res[-1]=-1
            return 
        
    
    
        i
    mergeSort(0,len(arr)-1)
    print(res[0])
        
        
        
        

 
