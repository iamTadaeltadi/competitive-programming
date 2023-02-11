class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        row=0
        columns=0
        tot_poss_diag=len(matrix)+len(matrix[0])-1
        
        for dig in range(tot_poss_diag):
           
            if dig>=len(matrix[0]):
                rr+=1
                cc=0
            else:
                rr=0
                cc=dig
            x=matrix[rr][cc]
            row,columns=rr,cc
            while row<len(matrix) and columns< len(matrix[0]):
                if x!=matrix[row][columns]:
                    return False
                row+=1
                columns+=1
        return True
        
        
            