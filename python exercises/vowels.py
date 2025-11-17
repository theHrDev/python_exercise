# 9. Count Vowels in a Word
vowels = ["a","e","i","o","u"]

user_word =  input("Enter a word: ")
for word in user_word:
    if word is vowels:
            print("Vowel")
    else:
            print("Consonant")