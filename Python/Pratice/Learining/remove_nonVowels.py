vowels = "AaEeIiOoUu"
setence = input("Enter setence: ")
index = 0
vowels_sentence = ""
for i in setence:
    char = setence[index]
    if char in vowels:
        vowels_sentence += char
        index += 1
print(vowels_sentence)