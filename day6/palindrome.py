def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower() #convert the string to lowercase for case-insensitive comparison
    return s == s[::-1]  # Check if the string is equal to its reverse

#Test the function
#user input
word=input("Enter a string:")
if is_palindrome(word):
    print(f'"{word}" is a palindrome.')
else:
    print(f'"{word}" is not a palindrome.')
