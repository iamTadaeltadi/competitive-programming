class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        n=len(edges)
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        for i in graph:
            start=i
            break
        queue=deque([start])
        while queue:
            curr=queue.popleft()
           
            if len(graph[curr]) ==n:
                return curr

            for i in graph[curr]:
                queue.append(i)