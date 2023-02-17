#Maahir Vohra
#CS100 Section 008
#HW 05, February 16, 2023


months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
horton = "A person's a person, no matter how small."
vowels = "aeiouAEIOU"



##1
for letter in months:
    firstLetter = letter[0][0]
    if firstLetter == 'J':
        print(letter)


##2
for i in range(100):
    if i % 2 == 0 and i % 5 == 0:
        print(i)


##3
for x in horton:
    if x in vowels:
        print(x)

