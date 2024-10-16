print('          SURVEY          ')
interestIT = input('Are you interested in computer science? (y/n): ')
games = input('Do you like playing computer games? (y/n): ')
instagram = input('Do you have an Instagram account? (y/n): ')
if interestIT=='y':
    interestIT="Yes"
else:
    interestIT='No'
if games=='y':
    games="Yes"
else:
    games='No'
if instagram=='y':
    instagram="Yes"
else:
    instagram='No'
print('          SURVEY  RESULTS        ')
print(f'Interested in computer science: {interestIT}')
print(f'Playing computer games: {games}')
print(f'Has an Instagram account: {instagram}')


