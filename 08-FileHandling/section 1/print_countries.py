with open("countries.txt", "r") as myf:
    for i, line in enumerate(myf):
        print(i, line, end=' ')