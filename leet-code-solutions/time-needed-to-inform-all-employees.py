class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        

        graph = defaultdict(list)


        for i in range(len(manager)):

            if manager[i] != -1:
                graph[manager[i]].append(i)

        answer = 0

        print(graph)
        

        def dfs_traversal(employee,time):
            nonlocal answer
            answer = max(time,answer)

            for negh in graph[employee]:
                dfs_traversal(negh,time + informTime[employee])
        

        dfs_traversal(headID,0)

        return answer

            
        




        

