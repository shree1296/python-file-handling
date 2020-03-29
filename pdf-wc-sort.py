
with open("file2.txt") as file:
    text = file.read()

    #text = file.extractText()

for char in "-.,\n":
    text = text.replace(char, " ")
text = text.lower()

word_list = text.split() # split returns a list of words by sequences of white spaces

# use dictionary for key ,value pairs

d = {}
for word in word_list:
    if word not in d:
        d[word] = 0
    d[word] += 1

""" for word in word_list:
    d[word] = d.get(word,0) + 1 """



word_freq = []
for key,value in d.items():
    word_freq.append((value,key))
#sort from higest ocuurences to lowest

word_freq.sort(reverse=True)
print(word_freq)
