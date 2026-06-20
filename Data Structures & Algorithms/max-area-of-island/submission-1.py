class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows,cols = len(grid), len(grid[0])

        area_island = 0 
        max_area=0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def area(r,c):

            if(r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==0):
                return 0

            grid[r][c] = 0
            area_island=1

            for dr,dc in directions:
                area_island+= area(r+dr,c+dc)       

            return area_island

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    area_island = area(r,c)
                    max_area=max(area_island,max_area)

        return max_area