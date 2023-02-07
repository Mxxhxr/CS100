#Maahir Vohra
#CS100 Section 008
#HW 02, February 1, 2023

#1
grades = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' ]

frequency = [grades.count('A'),grades.count('B'),grades.count('C'),grades.count('D'),grades.count('F')]
print(frequency)

##2
#a
dog_breeds = ['collie', 'sheepdog', 'Chow', 'Chihuahua']

#b
herding_dogs = [dog_breeds[:2]] #use slicing
print(herding_dogs)

#c
tiny_dogs = [dog_breeds[-1]] #using list indexing
print(tiny_dogs)

#d
print('Persian' in dog_breeds)