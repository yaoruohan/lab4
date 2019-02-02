import os
def walk(book):
    for name in os.lsitdir(book):
        path = os.path.join(book,name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)
    print(walk(book))