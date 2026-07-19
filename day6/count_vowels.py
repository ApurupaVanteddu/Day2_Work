def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

#user input
text = input("Enter a string: ")

#Function call 
vowel_count = count_vowels(text)
print(f'The number of vowels in "{text}" is: {vowel_count}')
