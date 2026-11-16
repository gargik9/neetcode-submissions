class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        no_of_islands = 0
        directions = [(0,1),(1,0),(-1,0),(0,-1)]


        def bfs(r,c):

            grid[r][c] = "0"

            for nr,nc in directions:
                nr+=r
                nc+=c
                while 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc]!="0":
                    grid[nr][nc] = "0"
                    bfs(nr,nc)


        for row in range(ROWS):
            for col in range(COLS):

                if grid[row][col]=="1":
                    bfs(row,col)
                    no_of_islands+=1

        return no_of_islands
