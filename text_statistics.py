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
    for word in line.split():
        # clean up
        word = word.strip('\n?!,."')
        word = word.lower()
        # if word in words_freq:        
        #     words_freq[word] += 1
        # else:
        #     words_freq[word] = 1
        try:
            words_freq[word] += 1
        except KeyError:
            words_freq[word] = 1

#print(words_freq)
print(len(words_freq))
# Step 2:
# another dictionary -> keys - freq(int), values - list of words []
freq = {}
for word, f in words_freq.items():
    if f not in freq:
        freq[f] = []    
    freq[f].append(word)

#print(freq)
# Step 3:
# sort it
# keys = list(freq.keys())
# keys.sort(reverse=True)

# items = list(freq.items()) <- (freq, [words])

# keys = sorted(freq.keys(), reverse=True)
# for i, key in enumerate(keys[:50]):    
#     print(i, "->", key, freq[key])

## using lambdas 

result = list(words_freq.items())
result.sort(reverse=True, key=lambda item : item[1])
print(result[:50])