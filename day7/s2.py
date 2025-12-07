import sys
from functools import cache

grid = [list(line) for line in sys.stdin.read().strip().splitlines()]
row = len(grid)
ccol = len(grid[0])

sr, sc = 0, grid[0].index('S')

@cache
def solve(r, c):
    if r >=  row:
        return 1
    if grid[r][c] == '^':
        return solve(r, c - 1) + solve(r, c + 1)
    else:
        return solve(r + 1, c)

print(solve(sr, sc))