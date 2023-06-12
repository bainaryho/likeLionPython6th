words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letters = {}

for word in words:
    letter = word[0]
    if letter not in by_letters:
        by_letters[letter] = [word]
    else:
        by_letters[letter].append(word)

    print(by_letters)

