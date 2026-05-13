class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        box_dict = defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue

                if val in row_dict[i]: return False
                row_dict[i].add(val)

                if val in col_dict[j]: return False
                col_dict[j].add(board[i][j])
                    
                if val in box_dict[(i//3, j//3)]: return False
                box_dict[(i//3, j//3)].add(val)
                
        return True