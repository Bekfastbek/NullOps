def main(word):
    return word == word[::-1]
word = input("Enter a word: ")
if main(word):
    print(f"'{word}' is a mirror!")
else:
    print(f"'{word}' is not a mirror!")