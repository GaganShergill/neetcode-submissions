class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            seen = set()
            for col in range(cols):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in seen:
                    return False
                seen.add(board[row][col])
        
        for col in range(cols):
            seen = set()
            for row in range(rows):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in seen:
                    return False
                seen.add(board[row][col])
        
        for square in range(rows):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    elif board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        
        return True


            
        


                
