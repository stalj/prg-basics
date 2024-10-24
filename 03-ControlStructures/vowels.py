index = 0
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0

while index < len(text):
    if text[index] in vowels:
        vowel_count += 1
    index += 1

print(f"The number of vowels in the text is: {vowel_count}")
