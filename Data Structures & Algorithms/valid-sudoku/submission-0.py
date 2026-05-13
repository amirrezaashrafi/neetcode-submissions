class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = {i: set() for i in range(9)}
        col_dict = {i: set() for i in range(9)}
        box_dict = {(i, j): set() for i in range(9) for j in range(9)}

        l = len(board)
        for i in range(l):
            for j in range(l):
                if board[i][j] == '.':
                    continue

                if board[i][j] in row_dict[i]:
                    return False
                else:
                    row_dict[i].add(board[i][j])

                if board[i][j] in col_dict[j]:
                    return False
                else:
                    col_dict[j].add(board[i][j])

                if board[i][j] in box_dict[(i//3, j//3)]:
                    return  False
                else:
                    box_dict[(i//3, j//3)].add(board[i][j])
        
        return True