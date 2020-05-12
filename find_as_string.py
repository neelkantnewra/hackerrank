#Output the integer number indicating the total number of occurrences of the substring in the original string.

def count_substring(string, sub_string):
    count = 0
    pos = 0
    while(True):
        pos = string.find(sub_string , pos)

        if pos > -1:
            count = count + 1
            pos += 1
        else:
            break


    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
