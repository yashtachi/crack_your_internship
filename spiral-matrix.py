class Solution:
    def spiralOrder(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        result = []
        x, y = 0, 0
        dx, dy = 1, 0
        for _ in range(rows * cols):
            result.append(matrix[y][x])
            matrix[y][x] = float('inf')
            if not (0 <= x + dx < cols and 0 <= y + dy < rows) or matrix[y + dy][x + dx] == float('inf'):
                dx, dy = -dy, dx
            x += dx
            y += dy
        return result