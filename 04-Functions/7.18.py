def check_palindrom(string):
    palindrom=True
    j=len(string)
    for i in range(0, len(string), 1):
        j-=1
        if string[i]!=string[j]:
            palindrom=False
            break

    return palindrom