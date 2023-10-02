class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:


        last=[0]*len(arr)

        min_val_so_far=float("inf")
        index=-1

        for i in range(len(arr)-1,-1,-1):

            

            if min_val_so_far >arr[i]:
                index=i
            min_val_so_far=min(min_val_so_far,arr[i])
            last[i]=min_val_so_far


        print(last,arr)

       

        

        for i in range(len(arr)-1,-1,-1):
            if arr[i] >last[i]:
                x=arr[i]
                indx=None
                y=0

                for j in range(i+1,len(arr)):
                    if arr[j]<x:
                        if arr[j]>y:
                            indx=j

                        y=max(arr[j],y)

                

                if  indx!=None:
                    temp=arr[i]
                    arr[indx]=temp
                arr[i]=y
                break

                
                
                # arr[i]=max(arr[i+1:])
                # arr[index]=temp
                # break


        return arr