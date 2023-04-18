wordOccurrences = [('rabbbit',1),('Alice',1),('rabbbit',4),('Alice',7),('Alice',10)]

def makeIndex(wordPageList):
    wordIndex = {}

    for item in wordPageList:
        word = item[0]
        page = item[1]
        if word not in wordIndex:
            wordIndex[word] = [page]
        else:
            wordIndex[word].append(page)
    return wordIndex

aliceIndex = makeIndex(wordOccurrences)

print(aliceIndex)

