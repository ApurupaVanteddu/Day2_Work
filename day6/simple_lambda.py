add = lambda x,y: x+y
print(add(5,3))#output: 8

find_largest_word=lambda sentence: max(sentence.split(), key=len)
sentence = input("Enter a sentence: ")
largest_word = find_largest_word(sentence)
print(f'The largest word in the sentence is: "{largest_word}"')
