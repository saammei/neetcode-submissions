class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [ [0] * 9 for _ in range(9) ]
        cols = [ [0] * 9 for _ in range(9) ]
        boxs = [ [0] * 9 for _ in range(9) ]

        for i in range(len(board)):
            for j in range(len(board[0])):
                x = board[i][j]
                if x == '.':
                    continue

                x = int(x) - 1
                k = (i//3)*3 + (j//3)

                if rows[i][x] or cols[j][x] or boxs[k][x]:
                    return False

                rows[i][x] = 1
                cols[j][x] = 1
                boxs[k][x] = 1

        return True

