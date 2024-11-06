check_list = []

def check_binary(string):
    for i in range(len(string)):
        if string[i] == '1' or string[i] == '0':
            check_list.append(True)
        else:
            check_list.append(False)
    if False in check_list:
        print('Not a binary number')
    else:
        print('Is a binary number')
    return 0