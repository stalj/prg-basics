print('SURVEY')
is_interested_in_CS = input('Are you interested in computer science? (y/n): ') 
likes_playing_games = input('Do you like playing computer games? (y/n): ')
has_instagram = input('Do you have an Instagram account? (y/n): ') 

is_interested_in_CS = 'Yes' if is_interested_in_CS == 'y' else 'No'
likes_playing_games = 'Yes' if likes_playing_games == 'y' else 'No'
has_instagram = 'Yes' if has_instagram == 'y' else 'No'

print('SURVEY RESULTS')
print(f"Is interested in Computer Science: {is_interested_in_CS}")
print(f"Playing computer games: {likes_playing_games}")
print(f"Has an instagram account: {has_instagram}")

