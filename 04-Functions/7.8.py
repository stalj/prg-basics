def is_binary(string):
    checker=0
    for i in range(len(string)):
        if string[i]=='1' or string[i]=='0':
            checker+=1
    if checker==len(string):
        return True
    else:
        return False

string_to_check=input('String: ')
binary=is_binary(string_to_check)
print(string_to_check,'Binary:', binary)