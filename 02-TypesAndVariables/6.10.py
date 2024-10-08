###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"
# display number of characters
print('Number of characters: ', len(movie))

# display title in capital letters
print("Title in capital letter: ", movie.upper())

# display title in small letters
print("Title in small letters: ", movie.lower())

# display how many times the vowel "e" appears in the title
print(f"e appears in the title {movie.count("e")} times")

# display where in the text is the word "Lord"
print(f"Lord is {movie.index("Lord")} position")

# display where in the text is the word "dragon"
if "dragon" in movie: print(f"dragon is {movie.index("dragon")} position")
else: print("dragon isn't in the title")