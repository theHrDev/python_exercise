# 9. Count Vowels in a Word
vowels = ["a","e","i","o","u"]

user_word =  input("Enter a word: ")
vowel_count = 0
for i in range(int(len(user_word))):
        # print(i)
    if user_word[i] == "a" or user_word[i] == "e" or user_word[i] == "i" or user_word[i] == "o" or user_word[i] == "u":
            vowel_count += 1
            print(f"{user_word[i]}")
            print(f"The number of vowel in the word {user_word} is {vowel_count}")
#     else:
#             print("Consonant")