from morse import letter_to_morse, unit

message = raw_input()
word = list(message)

for letter in word:
    print(letter)
    letter_to_morse(letter)
    unit()
    unit()
