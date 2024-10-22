def get_number_coins(amount_to_pay):
    coins_5 = 0
    coins_2 = 0
    coins_1 = 0
    if amount_to_pay >= 5:
        coins_5 = amount_to_pay // 5
        amount_to_pay = amount_to_pay % 5
    if amount_to_pay >= 2:
        coins_2 = amount_to_pay // 2
        coins_1 = amount_to_pay % 2
    
    return coins_1 + coins_2 + coins_5