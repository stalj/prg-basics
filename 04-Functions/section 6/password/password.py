def password_check(password):
    seen = []
    result = []
    if len(password) < 6:
        print('Invalid length')
        result.append(False)
    for i in range(len(password)):
        if password[i] in seen:
            print('Invalid characters')
            result.append(False)
        seen.append(password[i])
    if False in result:
        print('Invalid password')
    else:
        print('Valid password')