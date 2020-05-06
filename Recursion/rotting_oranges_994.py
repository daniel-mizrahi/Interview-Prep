class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col))
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        minutes = -1
        if len(queue) == 0:
            for row in grid:
                if 1 in row:
                    return -1
            return 0
        while len(queue) > 0:
            minutes += 1
            temp = list(queue)
            for item in temp:
                row, col = item
                for d in directions:
                    new_row = row + d[0]
                    new_col = col + d[1]
                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                        if grid[new_row][new_col] == 1:
                            grid[new_row][new_col] = 2
                            queue.append((new_row, new_col))
                queue.pop(0)
        for row in grid:
            if 1 in row:
                return -1
        return minutes
