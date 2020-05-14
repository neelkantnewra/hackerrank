#You are given a string S .
#Your task is to print all possible permutations of size K of the string in lexicographic sorted order.

from itertools import permutations

x,y = input().split()
z = (list(permutations(x,int(y))))
p = []
for i in range(0,len(z)):
    p.append(''.join(z[i]).lower())
p.sort()
for i in range(0,len(z)):
    print(p[i].upper())
