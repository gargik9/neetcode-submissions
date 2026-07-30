class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        directions = [(-1,0),(0,-1),(1,0),(0,1)]
        max_area = 0
        

        def dfs(r,c):

            grid[r][c]=0
            current_area = 1
           
            for dr,dc in directions:
                nr = r+dr
                nc = c+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                    current_area+=dfs(nr,nc)
                    
            return current_area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    max_area = max(max_area,dfs(r,c))

        return max_area       


