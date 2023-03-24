word_counts = {}
unique_words = set()

# Load a file
with open('song.txt', 'r') as file:
    # Go through every line in the file
    for line in file:
        # Separate lines in words and go through every word
        for word in line.split():
            # Add a word to the dictionary and increase its counter of appearances
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1
            # Add a word to the unique words group
            unique_words.add(word)

# Print out the words that appear only once in a file
print("Words that appear only once in a file: \n")
count_unique_words = 0
for word in unique_words:
    if word_counts[word] == 1:
        print(" " + word)
        count_unique_words += 1

# Print out the total number of words that appear only once in a file
print(f"\nTotal {count_unique_words} words that appear only once in a file.")
