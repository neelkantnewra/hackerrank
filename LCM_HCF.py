def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
    
def lcm(a,b):
    return a*b/gcd(a,b)
    
print(gcd(a,b),lcm(a,b))
