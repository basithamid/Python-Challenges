#https://www.hackerrank.com/challenges/making-anagrams/problem

#!/bin/python3

import sys
from collections import Counter

def makingAnagrams(s1, s2):
    # Complete this function
    s1 = Counter(s1)
    s2 = Counter(s2)
    s3 = ((s1-s2) + (s2-s1))
    return sum(s3.values())

s1 = input().strip()
s2 = input().strip()
result = makingAnagrams(s1, s2)

print(result)
