#Longest word in a sentence using a function
def longest_word(sentence):
    words = sentence.split()  # Split the sentence into words
    longest_word = max(words, key=len)  # Find the longest word using max with key as length
    return longest_word

#Accept user input
sentence = input("Enter a sentence: ")
#Function call
longest = longest_word(sentence)    
print(f'The longest word in the sentence is: "{longest}"')
