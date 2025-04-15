f = open('agencies.txt', 'r')

# Read all content, suitable for small files
content = f.read()
f.close()       # close the file after reading
print(content)
print('---' * 20)
# Read all lines, suitable for small files and processing line by line
f = open('agencies.txt', 'r')
lines = f.readlines() # read content to a list of lines
f.close()       # close the file after reading
for l in lines:
    print(l.strip()) # strip removes leading and trailing whitespace

print('---' * 20)
for l in lines:
    if 'Authority' in l:
        print(l.strip())
print('---' * 20)
# Read line by line, suitable for large files
f = open('agencies.txt', 'r')
for l in f: # read line by line
    if 'Authority' in l:
        print(l.strip())
f.close()       # close the file after reading
print('---' * 20)