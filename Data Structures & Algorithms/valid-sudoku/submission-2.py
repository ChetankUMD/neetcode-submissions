class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in row[r]
                    or board[r][c] in col[c]
                    or board[r][c] in square[(r//3,c//3)]):
                    return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                square[(r//3,c//3)].add(board[r][c])
            
        return True


        # m = len(board)
        # n = len(board[0])
        # for i in range(m):
        #     seen = set()
        #     for j in range(n):
        #         if board[i][j] == ".":
        #             continue
        #         if board[i][j] in seen:
        #             return False
        #         seen.add(board[i][j])
        
        # for i in range(m):
        #     seen = set()
        #     for j in range(n):
        #         if board[j][i] == ".":
        #             continue
        #         if board[j][i] in seen:
        #             return False
        #         seen.add(board[j][i])

        # for square in range(9):
        #     seen = set()
        #     for i in range(3):
        #         for j in range(3):
        #             row = (square//3) * 3 + i
        #             col = (square % 3) * 3 + j
        #             if board[row][col] == ".":
        #                 continue
        #             if board[row][col] in seen:
        #                 return False
        #             seen.add(board[row][col])
        # return True
 
