def encrypting(card_number):
    encrypted=card_number[1:3]+'**********'+card_number[12:16]
    return encrypted