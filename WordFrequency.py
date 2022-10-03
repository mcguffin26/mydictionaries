import re

word_frequency = {}
text_file = open('sometext.txt', 'r')
text = text_file.read().lower()
frequency = re.findall(r'\b[a-z]{1,15}\b', text)

for word in frequency:
    counter = word_frequency.get(word, 0)
    word_frequency[word] = counter + 1

frequency_list = word_frequency.keys()

for word in frequency_list:
    print(word, word_frequency[word])