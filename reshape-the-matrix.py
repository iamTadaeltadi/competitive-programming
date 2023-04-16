class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows=len(mat)
        cols=len(mat[0])
        ans=[]
        x=[]
        if c*r!=cols*rows:
            return mat
        for row in range(rows):
            for col in range(cols):
                x.append(mat[row][col])
                if c==len(x):
                    ans.append(x)
                    x=[]
        print(ans)
        return ans