class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        row, col = len(isWater), len(isWater[0])
        matrix = [[ -1 for _ in range(col)] for _ in range(row)]
        q = deque()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for i in range(row):
            for j in range(col):
                if isWater[i][j] == 1:
                    matrix[i][j] = 0
                    q.append((i, j))

        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                X, Y = x + dx, y + + dy
                if 0 <= X < row and 0 <= Y < col and matrix[X][Y] == -1:
                    matrix[X][Y] = matrix[x][y] + 1
                    q.append((X, Y))
            
        return matrix
