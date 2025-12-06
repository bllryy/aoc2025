import numpy as np #uhuhuhuhuhuhuhsdkgjhsgkgkdsg

#luke if ur reading this ur gey

f = open("in.txt").read()
lines = f.split("\n")
lines = np.array([list(line) for line in lines]).T
total = 0

for line in lines:
    op_char = line[-1]
    if op_char != " ":
        op = op_char
        if op == "*":
            base = 1
        else:
            base = 0

    num = "".join(char for char in line[:-1]).strip()
    if num:
        if op == "*":
            base *= int(num)
        else:
            base += int(num)
    else:
        total += base

total += base
print(total)