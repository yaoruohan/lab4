import os
def sed(pattern,replacement,book1,book2):
    fin = open(book1,'r')
    fout = open(book2,'w')
    for line in fin:
        if pattern in line:
            new_line = line.replace(pattern,replacement)
            fout.write(new_line)
        else:
            fout.write(line)
        except:
            print('something is wrong')
        fin.close()
        fout.close()
        if __name__ == '__main__':
            cwd = os.getcwd()
            print(cwd)
    pattern = 'oy'
    replacement = 'it'
    fin = 'book1.txt'
    fout = 'book2.txt'
sed(pattern,replacement,book1,book2)


