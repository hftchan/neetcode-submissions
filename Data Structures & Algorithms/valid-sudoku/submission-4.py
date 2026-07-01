class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)
        value = 0

        for r in range(9):
            for c in range(9):
                value= board[r][c]
                if value ==".":
                    continue
                square_pos = (r//3, c//3)
                if (value in row[r] or value in col[c] or value in square[square_pos]):
                    return False 
                
                row[r].add(value)
                col[c].add(value)
                square[square_pos].add(value)
        
        return True

                    
                
        