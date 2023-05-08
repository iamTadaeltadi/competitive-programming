class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        

        row = len(matrix)
        col = len(matrix[0])
        heap = []

        for i in range(row):
            for j in range(col):
                

                if k>len(heap):
                    heapq.heappush(heap,-1*matrix[i][j])
                else:
                    
                    if -1*heap[0]>matrix[i][j]:
                        heapq.heappushpop(heap, -1*matrix[i][j])
        print(heap)
        return -1*heap[0]