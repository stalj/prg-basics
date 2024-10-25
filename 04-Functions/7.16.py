def detector(people_bilans):
    amount_of_people=0
    detektor = False
    for i in range (len(people_bilans)):
        if people_bilans[i]=='+':
            amount_of_people+=1
        elif people_bilans[i]=='-':
            amount_of_people-=1
        if amount_of_people==3:
            detektor = True
            break
    return detektor