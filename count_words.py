import string
text = open("my_txt_file.txt", "r")

d = dict()
for line in text:
    line = line.strip()
    line = line.lower()

    # Remove the punctuation marks from the line
    line = line.translate(line.maketrans(" ", " ", string.punctuation))

    words = line.split(" ")

    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1

for key in list(d.keys()):
    print(key, ":", d[key])