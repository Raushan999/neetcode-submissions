class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ## Optimized code: using seen Set.

        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        
        # Iterate all the 9*9 matrix: -
        # Assign each cell values to their respective row or col or box it belong. 
        for i in range(9): 
            for j in range(9):

                val = board[i][j]
                if val == '.':  continue # ignore this value. 
                bx_idx = (i//3) + (j//3)*3
                if (val in row[i])  or (val in col[j]) or (val in box[bx_idx]):
                    return False
                
                row[i].add(val)
                col[j].add(val)
                box[bx_idx].add(val)
        return True


