def abbreviation (text):
    result = []
    txt = text.split(' ')
    for t in txt:
        result.append(t[0])
    print(''.join(result))