#content = open("proust.txt", encoding="UTF-8").read()
#print(len(content))

## TASK
## using dictionary (dictionaries and lists)
## print 50 most used words in this file!

i = 0       

words_freq = {}   # keys - strings, values - ints

# Step 1:
# assign to each word -> number of times it appeared in text

for line in open("proust.txt", encoding="UTF-8"):
    i += 1
    if i > 100:
        break    
    for word in line.split():
        # clean up
        word = word.strip('\n?!,."')
        word = word.lower()
        if word in words_freq:        
            words_freq[word] += 1
        else:
            words_freq[word] = 1

#print(words_freq)
print(words_freq["the"])
# Step 2:
# another dictionary -> keys - freq(int), values - list of words []

# Step 3:
# sort it