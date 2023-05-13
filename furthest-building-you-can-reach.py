class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap=[]
        difference=[]
        for i in range(1,len(heights)):

            difference.append(heights[i-1]-heights[i])
        print(difference)
       
        i=0

        while bricks>=0 and i<len(difference):
            if difference[i]<0:
                if ladders<=0 :
                    if heap and  heap[0]<-1*difference[i]:
                        x=heapq.heappop(heap)
                        bricks-=abs(x)
                        heapq.heappush(heap,-1*difference[i])

                    else:
                        bricks-=abs(difference[i])
                        


                else:
                    heapq.heappush(heap,-1*difference[i])
                    ladders-=1
            if bricks<0:
                return i
            i+=1
        return i