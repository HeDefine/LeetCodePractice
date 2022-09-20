# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#  
# 例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。
#  
# 示例 1：
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# 输出：true
#  
# 示例 2：
# 输入：board = [["a","b"],["c","d"]], word = "abcd"
# 输出：false
#  
# 提示：
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# board 和 word 仅由大小写英文字母组成

class Solution:
    def exist(self, board: list, word: str) -> bool:
        word_dict = dict()
        for row, line in enumerate(board):
            for col, val in enumerate(line):
                if word_dict.get(val) is None:
                    word_dict[val] = [[row, col]]
                else:
                    word_dict[val].append([row, col])
                    
        def recursion(cur_word, cur_list, cur_word_dict) -> bool:
            print(cur_list)
            if len(cur_word) == 0:
                return len(cur_list) == len(word)
            else:
                ch = cur_word[0]
                if cur_word_dict.get(ch) is None:
                    print('error')
                    return False
                positions = cur_word_dict[ch]
                for idx, position in enumerate(positions):
                    is_success = False
                    cur_word_dict[ch] = positions
                    if len(cur_list) == 0:
                        cur_word_dict[ch] = positions[:idx] + positions[idx+1:]
                        is_success = recursion(cur_word[1:], [position], cur_word_dict)
                    else:
                        last_position = cur_list[-1]
                        if abs(last_position[0] - position[0]) + abs(last_position[1] - position[1]) == 1:
                            cur_word_dict[ch] = positions[:idx] + positions[idx+1:]
                            is_success = recursion(cur_word[1:], cur_list + [position], cur_word_dict)
                    if is_success:
                        return True
                return False
        
        return recursion(word, [], word_dict)
                    

# print(Solution().exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))   # True
# print(Solution().exist(board = [["a","b"],["c","d"]], word = "abcd"))   # False
# print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE"))  # True
# print(Solution().exist([["C","A","A"],
#                         ["A","A","A"],
#                         ["B","C","D"]], "AAB")) 
# print(Solution().exist([["b"],
#                         ["a"],
#                         ["b"],
#                         ["b"],
#                         ["a"]], "baa"))
print(Solution().exist([["b","a","a","b","a","b"],
                        ["a","b","a","a","a","a"],
                        ["a","b","a","a","a","b"],
                        ["a","b","a","b","b","a"],
                        ["a","a","b","b","a","b"],
                        ["a","a","b","b","b","a"],
                        ["a","a","b","a","a","b"]], "aabbbbabbaababaaaabababbaaba"))
