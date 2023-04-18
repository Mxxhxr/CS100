# Maahir Vohra
# CS100 Section 008
# HW 08, March 23, 2023

def twoWordsV2(length, firstLetter):
    lst = []
    firstWord = ''
    secondWord = ''
    while len(firstWord) != length:
        firstWord = input("Enter a " + str(length) + "-letter word please: ")
        if len(firstWord) != length:
            continue
    lst.append(firstWord)

    while secondWord == '' or secondWord[0].lower() != firstLetter.lower():
        secondWord = input("Enter a word beginning with " +
                           firstLetter + " please: ")
        continue

    lst.append(secondWord)
    return lst
