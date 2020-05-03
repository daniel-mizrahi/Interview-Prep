import copy
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        starting_locations = {}
        def dfs(word, row, col, visited) -> bool:
            if word == "":
                return True
            visited[(row, col)] = True   
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            possible = False
            for d in directions:
                new_row = row + d[0]
                new_col = col + d[1]
                if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]):
                    if board[new_row][new_col] == word[0] and (new_row, new_col) not in visited:
                        possible = possible or dfs(word[1:], new_row, new_col, copy.deepcopy(visited))
            return possible
        
        ret = False
        for row, l in enumerate(board):
            for col, val in enumerate(l):
                if val == word[0]:
                    visited = {}
                    ret = ret or dfs(word[1:], row, col, visited)
        return ret
