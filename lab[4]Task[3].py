from collections import Counter
fin = open('book.txt')
c = Counter()
for line in fin:
 words = line.split()
 c += Counter(words)
for words in c.most_common(20):
    print(words,end = '&')













