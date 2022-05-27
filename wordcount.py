# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content():
    # [assignment] Add your code here 
    with open('story.txt') as f:
        contents = f.read()
        print(contents)

read_file_content()


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

def count_words():
    import string
    text = open("./story.txt")
    # [assignment] Add your code here

    # create a dictionary
    d = dict()

    # loop through each line of the file
    for line in text:
        line = line.strip()

        line = line.lower()

        # Remove the punctuation marks from the line
        line = line.translate(line.maketrans("", "", string.punctuation))

        # split line into word
        words = line.split()
        for word in words:
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1

                # print dictionary content
    for key in list(d.keys()):
        print(key, ":", d[key])


count_words()