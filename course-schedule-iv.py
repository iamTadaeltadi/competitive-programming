class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        


        adjMatrix = [[float("inf") for i in range(numCourses)]for i in range(numCourses)]


        for i in range(len(prerequisites)):
            adjMatrix[prerequisites[i][0]][prerequisites[i][1]] =1
        ans = []


        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                        adjMatrix[i][j] = min(adjMatrix[i][j], adjMatrix[i][k] + adjMatrix[k][j])
        

        for i in range(len(queries)):
            row,col = queries[i][0],queries[i][1]
            if adjMatrix[row][col] != float("inf"):
                ans.append(True)
            else:
                ans.append(False)

        return ans