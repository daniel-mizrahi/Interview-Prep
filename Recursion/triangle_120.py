class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def bfs(triangle, row, col):
            if row == len(triangle) - 1:
                memo[(row,col)] = triangle[row][col]
            else:
                left, right = 0,0
                if (row + 1, col) in memo:
                    left = memo[(row + 1, col)]
                else:
                    left = bfs(triangle, row + 1, col)
                if (row + 1, col+1) in memo:
                    right = memo[(row + 1, col+1)]
                else:
                    right = bfs(triangle, row + 1, col+1)
                memo[(row, col)] = triangle[row][col] + min(left, right)
            return memo[(row, col)]
        return bfs(triangle, 0,0)
