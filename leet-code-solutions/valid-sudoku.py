class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        square = defaultdict(set)

        for row in range(9):
            for col in range(9):

                if  board[row][col]==".":
                        continue

                for c in range(9):
                    if c != col and board[row][c] == board[row][col]:
                        return False
                
                # checks if there is a duplicate number in the same row
                for r in range(9):
                    if r != row and board[r][col] == board[row][col]:
                        return False

                if board[row][col] in square[(row // 3, col // 3)]:
                    return False
                square[(row // 3, col // 3)].add(board[row][col])
        return True