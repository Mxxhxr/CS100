# Maahir Vohra
# CS100 Section 008
# HW 10, April 17, 2023

test1 = ['I', 'say', 'what', 'I', 'mean', 'i', 'MEAN']
test2 = ['Hi', 'Hello', 'You', 'yellow', 'and', 'AWESOME']
test3 = ['come', 'COME', 'C', 'rescue', 'RE', 'm']


def initialLetterCount(wordList):
    letterCount = {}

    for word in wordList:
        if word[0] not in letterCount:
            letterCount[word[0]] = 1
        else:
            letterCount[word[0]] += 1
    return letterCount


print(initialLetterCount(test1))
print(initialLetterCount(test2))
print(initialLetterCount(test3))
