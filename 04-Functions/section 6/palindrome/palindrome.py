def pali(text):
    for i in range(len(text)):
        if text[i] == text[len(text) - i - 1]:
            return 'This word is a palindrome'
        else:
            return 'This word is not a palindrome'