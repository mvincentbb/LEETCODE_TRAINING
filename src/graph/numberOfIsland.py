import collections


class Solution:
    #implement the solution
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        # rows est tout ce qui se supperpose et donc se suit
        # cols c'est est le nombre d'element  a l'interieur d'un element
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0
        # BFS
        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dc, dr in directions:
                    r, c = row + dr , col + dc
                    if(r in range(rows)
                        and c in range(cols)
                        and grid[r][c] == "1"
                        and (r,c) not in visit
                    ):
                        q.append((r,c))
                        visit.add((r,c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        return islands

