# Maahir Vohra
# CS100 Section 008
# HW 10, April 17, 2023

test1 = ['I', 'hi', 'HI', 'I', 'mean', 'i', 'maahir', 'teeth']
test2 = ['Hello', 'hi', 'your', 'yellow', 'And', 'AWESOME', 'orange']
test3 = ['come', 'COME', 'C', 'rescue', 'REBOUND', 'c', 'COOL']


def shareOneLetter(wordList):
    sharedWordDic = {}

    for word in wordList:
        sharedWordDic[word] = []
        for otherWord in wordList:
            if word != otherWord and any(letter in word for letter in otherWord):
                if otherWord not in sharedWordDic[word]:
                    sharedWordDic[word].append(otherWord)
        for i, v in enumerate(sharedWordDic[word]):
            if v in sharedWordDic[word][i+1:]:
                sharedWordDic[word].pop(i)
    return sharedWordDic


print(shareOneLetter(test1))
print(shareOneLetter(test2))
print(shareOneLetter(test3))
