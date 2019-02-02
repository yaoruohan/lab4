#open the book for the whole
import string
fin = open('book.txt')
for word in fin:
    word = word.strip()
    print(word)
# count different words appeared times in book
from collections import Counter
fin = open('book.txt')
c = Counter()
for line in fin:
    words = line.split()
    c += Counter(words)
print(c)

for words in c.most_common():
    print(words,end = '&')
#count total numbers of words
fname = input("please enter a book name: ")
num_words = 0
with open(fname,'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
    print("Total number of words is: ")
    print(num_words)













