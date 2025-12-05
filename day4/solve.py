#!/usr/bin/env python3

with open("input.txt", "r") as f:
    dih = f.read()

G = [list(row) for row in dih.splitlines()]
R = len(G)
C = len(G[0])

def count_neighbors(grid, r, c):
    nbr = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            rr, cc = r + dr, c + dc
            if 0 <= rr < R and 0 <= cc < C and grid[rr][cc] == '@':
                nbr += 1
    return nbr

# Part 1: count rolls accessible in the initial layout
p1 = 0
for r in range(R):
    for c in range(C):
        if G[r][c] != '@':
            continue
        if count_neighbors(G, r, c) < 4:
            p1 += 1
print(p1)

# Part 2: repeatedly remove all currently accessible rolls until none remain
grid2 = [row.copy() for row in G]
p2 = 0
while True:
    to_remove = []
    for r in range(R):
        for c in range(C):
            if grid2[r][c] == '@' and count_neighbors(grid2, r, c) < 4:
                to_remove.append((r, c))
    if not to_remove:
        break



    for r, c in to_remove:
        grid2[r][c] = '.'
    p2 += len(to_remove)

print(p2)