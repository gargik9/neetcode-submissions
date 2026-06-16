
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return

        INF = 2**31 - 1
        m, n = len(grid), len(grid[0])
        q = deque()

        # 1) Multi-source: push all treasures (0s)
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c))

        # 2) BFS outward
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                # bounds check
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                # only fill unvisited empty cells (INF)
                if grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
