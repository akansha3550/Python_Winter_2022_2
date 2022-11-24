keys_in_file = {}
with open ('Kennedy.txt', 'r') as f:
    for i,line in enumerate(f):
        words = line.strip().split()
        for word in set(words):
            keys_in_file.setdefault(word, []).append(i+1)

print (keys_in_file)
words = line.lower().strip().split()
for k in sorted(keys_in_file):
    print (k+':', *keys_in_file[k])