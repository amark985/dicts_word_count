"""Count words in file."""

read_file = open("twain.txt")

word_count = {}

# Loop through the text
for line in read_file:
    word_splits = line.split(' ')
    
    # Loop through the words in each line
    for word in word_splits:
        word_count[word] = word_count.get(word, 0) + 1


print(word_count)