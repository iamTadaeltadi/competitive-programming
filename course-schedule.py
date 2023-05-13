class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph=defaultdict(list)
        queue=deque()
        
        
        incoming=[0]*numCourses

        for i in prerequisites :
            graph[i[1]].append(i[0])
            incoming[i[0]]+=1
        
        for i,v in enumerate(incoming):
            if not v:
                queue.append(i)
        count=0
        while queue:
            curr=queue.popleft()
            count+=1

            for preq in graph[curr]:
                incoming[preq]-=1
                if incoming[preq]==0:
                    queue.append(preq)
       
        if count==numCourses:
            return True
        return False