def mask(card):
    if len(card) != 16 or not card.isdigit():
        print('invalid card')
    else:
        return card[:2] + '*' * 10 + card[-4:]