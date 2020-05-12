#text wrap with string and length of the line 


import textwrap

def wrap(string, max_width):
    z = textwrap.TextWrapper(max_width)
    p = z.wrap(string)
    c =""
    for i in range(0,len(p)):
        print(c + p[i])
    return c

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
