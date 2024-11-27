def num_words(text):
    return len(text.split(' '))

def longest(text):
    num = num_words(text)
    text = text.split(' ')
    for i in range(num - 1):
        for j in range(num - i - 1):
            if len(text[j]) < len(text[j + 1]):
                text[j], text[j + 1] = text[j + 1], text[j]
    return ' '.join(map(str, text))

def alphabetic(text):
    text = text.split(' ')
    n = len(text)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if text[j] < text[min_index]:
                min_index = j
        text[i], text[min_index] = text[min_index], text[i]
    return text