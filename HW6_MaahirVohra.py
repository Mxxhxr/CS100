#Maahir Vohra
#CS100 Section 008
#HW 06, February 22, 2023

#1
def hasFinalLetter(strList, letters):
    newLst = []
    for i in strList:    
        if i[-1] in letters:
            newLst.append(i)
    return newLst
    

#test 1
test1 = ["Plop", "SEE", "HIPPY", "hAPPy"] 
letters1 = "ADEJLPTYadejlpty"
print(hasFinalLetter(test1, letters1)) #should return all

#test 2
test2 = ["Zooz", "Annex", "globber" ] 
letters2 = "ABCDEFGHIabcdefghi"
print(hasFinalLetter(test2, letters2)) #should return empty list

#test 3
test3 = ["hOOkaH", "bIngus", "HelloLOL"] 
letters3 = "ADEIPQRLadeipqrl"
print(hasFinalLetter(test3, letters3)) #should return only last one

#################################################################################

#2
def isDivisible(maxInt, twoInts):
    newList = []
    for num in range(1, maxInt):
        if num % twoInts[0] == 0 and num % twoInts[1] == 0:
            newList.append(num)
    return newList


#test 1
max1 = 100
ints1 = (2, 5)
print(isDivisible(max1, ints1)) #should return multiples of 10

#test 2
max2 = 150
ints2 = (3, 10)
print(isDivisible(max2, ints2)) #should return multiples of 30


#test 3
max3 = 13
ints3 = (7, 8)
print(isDivisible(max3, ints3)) #should return mulitples of 56 (none in this range)


