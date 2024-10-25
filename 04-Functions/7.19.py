def remove_spaces(sentence):
    sentence_without=''
    j=0
    for i in range(len(sentence)):
        if sentence[i]!=' ':
            sentence_without+=sentence[i]
            
    return sentence_without
