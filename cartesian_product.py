#Output the space separated tuples of the cartesian product.

from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*list(product(a, b)))                 #red line will show but avoid it just Run , * is for unpack of list
