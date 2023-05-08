class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # heapq.heapify(tasks,key=lambda x: x[0])
        for i,v in enumerate(tasks):
            v.append(i)
        i=0
        tasks.sort(key=lambda x:x[0])
        print(tasks)
        cur_time=tasks[0][0]
        last_time=tasks[-1][0]
        heap=[]
        res=[]
        while heap or i<len(tasks):
            while i<len(tasks) and tasks[i][0]<=cur_time:
                heapq.heappush(heap,[tasks[i][1],tasks[i][2]])
                i+=1
            if not heap:
                cur_time=tasks[i][0]
            else:
                process_time,index=heapq.heappop(heap)
                res.append(index)
                cur_time+=process_time
        return res