def letter_in_text(sentence, letter):
    how_many=0
    letter=letter.upper()
    sentence=sentence.upper()
    for i in range(0,len(sentence)):
        if sentence[i]==letter:
            how_many+=1
    return how_many
