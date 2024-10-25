def acronyms(sentence2):
    sentence2=sentence2.strip()
    tabela = sentence2.split(" ")
    acr = ''
    for slowo in tabela:
          acr+=slowo[0]
    
    return acr