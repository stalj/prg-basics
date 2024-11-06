def find_letter(letter, text):
    n = 0
    for i in range(len(text)):
        if letter == text[i]:
            n += 1
    return n