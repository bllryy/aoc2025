"""
parse
counts how many of those integers fall inside any interval (a).
merges the intervals in order and counts how many total integer positions they cover (b).

https://stackoverflow.com/questions/11315010/what-do-and-before-a-variable-name-mean-in-a-function-signature
https://www.reddit.com/r/learnpython/comments/dor6bu/how_does_the_star_before_argument_not_a_parameter/
wicked pull
https://www.w3schools.com/python/ref_func_sorted.asp
"""

F, I = open('in.txt').read().split('\n\n')
F = [[*map(int, f.split('-'))] for f in F.split()]

a = sum(any(i in range(*f) for f in F) # f will b unpacked 
        for i in map(int, I.split()))

b = i = 0
for s, e in sorted(F):
    if s <= i: s = i + 1
    if s <= e:
        i = max(i, e)
        b += e - s + 1

print(a, b)
