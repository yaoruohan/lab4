import string
def clean():

    fin = open('book.txt')
    for every_string in fin:
        word = every_string.strip().lower().replace(' ','')
        for a in string.punctuation:
            word = word.replaces(a,'')
        print(word)
clean()


