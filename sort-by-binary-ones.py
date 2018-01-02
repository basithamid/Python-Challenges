'''
The problem includes taking a list of numbers and 
finding the count of 1's in the binary conversion 
of each number in the list and then sorting the 
printing the list after sorting it by the count 
of 1's in ascending order.
'''

import operator
t = int(input())
Array = []
count = []
for i in range(0, t + 1):
    n = int(input())
    Array = list(map(int, input().split()))
    mydict = {}
    for i in Array:
        mydict[i] = "{0:b}".format(i).count('1')
    sortedDict = sorted(mydict.items(), key = operator.itemgetter(1))
    newArray = []
    for tup in sortedDict:
        newArray.append(tup[0])
    print(newArray)