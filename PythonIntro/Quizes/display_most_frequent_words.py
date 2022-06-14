# This solution attempts toread from a file and displays the most frequent 100 workds that are 5 characters or greater

# Step1: Create an empty dictionary to store words and word counts
word_count = {}

# Step2: Iterate over the file as shown in the slide for this task
for line in open('grep.py', encoding='utf8'):
    # Step 3: Use the split() method to break one line into a list of strings
    words = line.split()

    for word in words:
        # Step4: Iterate over the list of strings, check if the word is in the dictionary already
        if word in word_count:
            # Step5: Increment the count value for that word if it's in the dictionary
            word_count[word] += 1
        else:
            # Step6: If it's not in the dictionary add it to dictionary
            word_count[word] = 1

# Step7: To sort the dictionary, convert it to a list of tuples using word_count.items() and pass this into sorted()
# Step8: To sort based on the values, we'll need a key= function. We need to sort by the values, in other words.
# the second item in the tuple.
sorted_words = sorted(word_count.items(), key=lambda a: a[1], reverse=True)

# step9 print the first 100 items in the list
five_letters = [(word, count) for word, count in sorted_words if len(word) >= 5]
for word in five_letters:
    print(word[:100])
