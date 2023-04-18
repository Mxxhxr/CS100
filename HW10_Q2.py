# Maahir Vohra
# CS100 Section 008
# HW 10, April 17, 2023

test1 = ['I', 'hi', 'HI', 'I', 'mean', 'i', 'maahir']
test2 = ['Hello', 'hi', 'your', 'yellow', 'And', 'AWESOME']
test3 = ['come', 'COME', 'C', 'rescue', 'RE', 'c']


def initialLetters(wordList):
    initialDic = {}

    for word in wordList:
        if word[0] not in initialDic:
            initialDic[word[0]] = [word]
        elif word not in initialDic[word[0]]:
            initialDic[word[0]].append(word)

    return initialDic


print(initialLetters(test1))
print(initialLetters(test2))
print(initialLetters(test3))
