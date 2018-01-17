"""
Problem:
Link to problem:
[complexRoots](https://www.hackerearth.com/codearena/ring/9a2b9d3/)
"""

import cmath
count = 0
n = int(input())
for i in range(0, n):
    abc = list(map(int, input().split()))
    root = cmath.sqrt((abc[1]*abc[1]) - (4 * abc[0] * abc[2]))
    strroot = str(root)
    ind = strroot.index('j') - 1
    if strroot[ind] == '0':
        count = count + 1
print(count)
