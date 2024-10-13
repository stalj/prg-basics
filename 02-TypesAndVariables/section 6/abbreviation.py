uni = "Krakow University of Economics"

def abbreviation(text=''):
    result = []
    list_of_words = text.split(' ')
    for word in list_of_words:
        if word[0].isupper():
            result.append(word[0])
    print(''.join(result))

abbreviation(uni)