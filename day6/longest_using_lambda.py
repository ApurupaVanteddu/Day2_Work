import time

def find_longest_word(sentence):
    words = sentence.split()  # Split the sentence into words

    # Check if the sentence is empty
    if not words:
        return None

    # Find the longest word
    longest_word = max(words, key=len)
    return longest_word


# User input
sentence = input("Enter a sentence: ")

# Start time
start_time = time.perf_counter()

# Function call
longest = find_longest_word(sentence)

# End time
end_time = time.perf_counter()

# Display result
if longest:
    print("Longest word:", longest)
else:
    print("No words entered.")

# Display execution time
print(f"Execution time: {end_time - start_time:.6f} seconds")
