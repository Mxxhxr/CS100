# Maahir Vohra
# CS100 Section 008
# HW 08, March 23, 2023

def twoWords(length, firstLetter):
    lst = []
    while True:
        firstWord = input("Enter a " + str(length) + "-letter word please: ")
        if len(firstWord) != length:
            continue

        lst.append(firstWord)
        while True:
            secondWord = input("Enter a word beginning with " +
                               firstLetter + " please: ")
            if secondWord[0].lower() == firstLetter.lower():
                lst.append(secondWord)
                return lst
            else:
                continue
