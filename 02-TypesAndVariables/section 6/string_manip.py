movie = "The Lord of the Rings: The Return of the King"

print('Number of characters: ', len(movie))

print('Title in capital letters: ', movie.upper())

print('Title in lower letters: ', movie.lower())

num = movie.count('e')
print(f'The letter "e" appears {num} times')

index = movie.find('Lord')
print(f'The word "Lord" was found at position {index}')

index = movie.find('dragon')

if index == -1:
    print('The word "dragon" was not found')
else:
    print(f'The word "dragon" was found at position {index}')