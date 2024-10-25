def most_dices(dice):
    winner=0
    for i in range(1,7):
        x=dice.count(str(i))
        if dice.count(str(i))>dice.count(str(i-1)):
            winner=i
    
    return winner
