class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        heap = [[0,firstPerson],[0,0]]
        


        graph = defaultdict(list)
        for i in range(len(meetings)):
            graph[meetings[i][0]].append([meetings[i][1],meetings[i][2]])
            graph[meetings[i][1]].append([meetings[i][0],meetings[i][2]])


        seen = [float("inf")]*n



        while heap:
            
            time,curr = heapq.heappop(heap)
            print(curr)

            seen[curr] = time

            for child,time_of_end in graph[curr]:
                if time<=time_of_end and  seen[child]>time_of_end :
                    heapq.heappush(heap,[time_of_end,child])
                
        print(seen)
                    
        return [index for index,i in enumerate(seen) if i != float("inf")]