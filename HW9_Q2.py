def file_stats(in_file):
    iFile = open(in_file, 'r')
    data = iFile.read()

    numLines = data.count('\n') + 1

    words = data.split()
    numWords = len(words)

    numChars = len(data)
    iFile.close()

    print("Number of lines: " + str(numLines))
    print("Number of words: " + str(numWords))
    print("Number of characters: " + str(numChars))
