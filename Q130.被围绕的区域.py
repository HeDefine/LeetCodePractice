#!/usr/bin/env python3

# https://leetcode-cn.com/problems/surrounded-regions
# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
#
# 示例:
# X X X X
# X O O X
# X X O X
# X O X X
# 运行你的函数后，矩阵变为：
# X X X X
# X X X X
# X X X X
# X O X X
#
# 解释:
# 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。


class Solution:
    def solve(self, board: [[str]]) -> None:
        allO = set()
        boardO = set()
        for x, line in enumerate(board):
            for y, val in enumerate(line):
                if val == 'O':
                    allO.add((x, y))
                    if x == 0 or x == len(board) - 1 or y == 0 or y == len(line) - 1:
                        boardO.add((x, y))
        while len(boardO) > 0:
            pos = boardO.pop()
            if pos in allO:
                allO.remove(pos)
                if pos[0] - 1 > 0 and board[pos[0] - 1][pos[1]] == 'O':
                    boardO.add((pos[0] - 1, pos[1]))
                if pos[0] + 1 < len(board) - 1 and board[pos[0] + 1][pos[1]] == 'O':
                    boardO.add((pos[0] + 1, pos[1]))
                if pos[1] - 1 > 0 and board[pos[0]][pos[1] - 1] == 'O':
                    boardO.add((pos[0], pos[1] - 1))
                if pos[1] + 1 < len(board[0]) - 1 and board[pos[0]][pos[1] + 1] == 'O':
                    boardO.add((pos[0], pos[1] + 1))

        for (x, y) in allO:
            board[x][y] = 'X'


t = [["X", "X", "X", "X"],
     ["X", "O", "O", "X"],
     ["X", "X", "O", "X"],
     ["X", "O", "X", "X"]]
Solution().solve(t)

t1 = [["X", "O", "X", "O", "X", "O"],
      ["O", "X", "O", "X", "O", "X"],
      ["X", "O", "X", "O", "X", "O"],
      ["O", "X", "O", "X", "O", "X"]]
Solution().solve(t1)

for i, o in enumerate(t1):
    print(o)
