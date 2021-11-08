# A 和 B 在一个 3 x 3 的网格上玩井字棋。
# 井字棋游戏的规则如下：
# 玩家轮流将棋子放在空方格 (" ") 上。
# 第一个玩家 A 总是用 "X" 作为棋子，而第二个玩家 B 总是用 "O" 作为棋子。
# "X" 和 "O" 只能放在空方格中，而不能放在已经被占用的方格上。
# 只要有 3 个相同的（非空）棋子排成一条直线（行、列、对角线）时，游戏结束。
# 如果所有方块都放满棋子（不为空），游戏也会结束。
# 游戏结束后，棋子无法再进行任何移动。
# 给你一个数组 moves，其中每个元素是大小为 2 的另一个数组（元素分别对应网格的行和列），它按照 A 和 B 的行动顺序（先 A 后 B）记录了两人各自的棋子位置。
# 如果游戏存在获胜者（A 或 B），就返回该游戏的获胜者；如果游戏以平局结束，则返回 "Draw"；如果仍会有行动（游戏未结束），则返回 "Pending"。
# 你可以假设 moves 都 有效（遵循井字棋规则），网格最初是空的，A 将先行动。
#  
# 示例 1：
# 输入：moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
# 输出："A"
#
# 示例 2：
# 输入：moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
# 输出："B"
#
# 示例 3：
# 输入：moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
# 输出："Draw"
# 输出：由于没有办法再行动，游戏以平局结束。
#
# 示例 4：
# 输入：moves = [[0,0],[1,1]]
# 输出："Pending"
# 解释：游戏还没有结束。
# 
# 提示：
# 1 <= moves.length <= 9
# moves[i].length == 2
# 0 <= moves[i][j] <= 2
# moves 里没有重复的元素。
# moves 遵循井字棋的规则。

class Solution:
    def tictactoe(self, moves: list) -> str:
        plate = [[1,2,3],[4,5,6],[7,8,9]]
        for idx, point in enumerate(moves):
            x, y = point[0], point[1]
            plate[x][y] = 'A' if idx % 2 == 0 else 'B'
            
            if plate[x][0] == plate[x][1] == plate[x][2] != 0:
                return plate[x][y]
            elif plate[0][y] == plate[1][y] == plate[2][y]:
                return plate[x][y]
            elif plate[0][0] == plate[1][1] == plate[2][2]:
                return plate[x][y]
            elif plate[0][2] == plate[1][1] == plate[2][0]:
                return plate[x][y]
        return 'Draw' if len(moves) == 9 else 'Pending'
            

print(Solution().tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))    # A
print(Solution().tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))    # B
print(Solution().tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))    # Draw
print(Solution().tictactoe([[0,0],[1,1]]))  # Pending