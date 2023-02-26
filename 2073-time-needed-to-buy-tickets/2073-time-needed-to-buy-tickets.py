class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        x=deque()
        
        for i in range(len(tickets)):
            x.append([tickets[i],i])
        count=0
        while x :
            x[0][0]-=1
            if x[0][0]==0 and k==x[0][1]:
                count+=1
                break
            if x[0][0]==0:
                x.popleft()
            else:
                x.append(x.popleft())
            count+=1
        return count
            
                
            
                
            
            
                 