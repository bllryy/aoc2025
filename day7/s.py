"""
https://www.geeksforgeeks.org/python/deque-in-python/#
https://docs.python.org/3/library/collections.html
python3 s.py < in.txt 
"""
import sys
from collections import deque

grid = [list(line) for line in sys.stdin.read().strip().splitlines()]
row = len(grid)
ccol = len(grid[0])

sr, sc = 0, grid[0].index('S')

splits = 0
q = deque()
seen = set()
q.append((sr, sc))

while q:
    r,c = q.popleft()
    if not (0 <= r < row and 0 <= c < ccol):
        continue
    if (r,c) in seen:
        continue
    seen.add((r,c))
    if grid[r][c] == '^':
        splits += 1
        q.append((r, c - 1))
        q.append((r, c + 1))
    else:
        q.append((r + 1, c))
        
    
print(splits)