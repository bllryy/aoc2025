"""
we can just see if each number is in each range
iterated over all ranges to check if the given 
ingredient is part of it or not

Read the whole file
Split on the blank line
Parse ranges and ingredients separately
Count ingredients that fall in at least one range

The database operates on ingredient IDs. It consists of a list of fresh ingredient ID ranges, a 
blank line, and a list of available ingredient IDs. For example:

https://stackoverflow.com/questions/11315010/what-do-and-before-a-variable-name-mean-in-a-function-signature
https://www.reddit.com/r/learnpython/comments/dor6bu/how_does_the_star_before_argument_not_a_parameter/
wicked pull
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