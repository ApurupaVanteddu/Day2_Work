#Accept a list of integers from the user
numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split()))

#Use filter() with a lambda func to selct even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

#use map() with a lambda function to square each even number
squared_evens = list(map(lambda x: x ** 2, even_numbers))
print("Squared even numbers:", squared_evens)
