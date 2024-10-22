import securingcard
card=input('Card number: ')
while len(card)!=16:
    card=input('Invalid card number. Try again: ')
encrypted_card=securingcard.encrypting(card)
print(encrypted_card)