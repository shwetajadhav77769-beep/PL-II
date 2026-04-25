# 1. Program to find length of a string
string = input("Enter a string: ")
print("Length of the string is:", len(string))

# 2. Program to reverse a string
string = input("Enter a string: ")
reverse = string[::-1]

print("Reversed string is:", reverse)

# 3. Program to check whether a string is palindrome
string = input("Enter a string: ")

if string == string[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

# 4. Program to count vowels and consonants in a string
string = input("Enter a string: ").lower()

vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for char in string:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)

# 5. Program to convert string to upper and lower case
string = input("Enter a string: ")

print("Upper case:", string.upper())
print("Lower case:", string.lower())

# 6. Program to count frequency of characters in a string
string = input("Enter a string: ")

frequency = {}

for char in string:
    frequency[char] = frequency.get(char, 0) + 1

print("Character frequencies:")
for key, value in frequency.items():
    print(key, ":", value)

# 7. Program to remove spaces from a string
string = input("Enter a string: ")

result = string.replace(" ", "")

print("String without spaces:", result)

# 8. Program to replace a word in a string
string = input("Enter a sentence: ")
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

result = string.replace(old_word, new_word)

print("Updated string:", result)

# 9. Program to split and join strings
string = input("Enter a sentence: ")

# Split string into list
words = string.split()

print("Split words:", words)

# Join list into string
joined_string = "-".join(words)

print("Joined string:", joined_string)

# 10. Program to check whether two strings are anagrams
string1 = input("Enter first string: ").lower()
string2 = input("Enter second string: ").lower()

if sorted(string1) == sorted(string2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")
