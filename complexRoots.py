"""
Problem:
Link to problem:
(https://www.hackerearth.com/codearena/ring/9a2b9d3/)
The problem states that if a quadratic equation has complex/imaginary roots then that problem is not solved by a kid named Bosby or something.
so given the values of a,b,c for a test case, find how many equations can be solved by the kid.
"""

import cmath
count = 0
n = int(input())
for i in range(0, n):
    abc = list(map(int, input().split()))
    root = cmath.sqrt((abc[1]*abc[1]) - (4 * abc[0] * abc[2]))
    strroot = str(root)
    ind = strroot.index('j') - 1
    if strroot[ind] == '0' and strroot[ind-1] == '+':
        count = count + 1
print(count)
