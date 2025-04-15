# Ex: read authors.txt, find and print authors that use gmail
f = open('authors.txt', 'r')
lines = f.readlines() # read content to a list of lines
f.close()       # close the file after reading


print(f'{"Authors":30}{"Email":50}')
for line in lines:
    if 'gmail' in line:
        author = line.split('<')[0] # split line by < and get the first part
        email = line.split('<')[1].replace('>', '') # split line by < and get the second part
        print(f'{author.strip():30}{email.strip():50}') # strip removes leading and trailing whitespace