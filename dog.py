# Maahir Vohra
# CS100 Section 008
# HW 11, April 19, 2023

class Dog:
    ''' Class that gives each dog its own attributes.'''

    speicies = "Canis familiaris"
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.tricks = []
    
    def teach(self, trickName):
        self.tricks.append(trickName)
        message = print(self.name, "knows", trickName)
        return message
    
    def knows(self,trickName):
        for word in self.tricks:
            if word.lower() == trickName.lower():
                print("Yes,", self.name, "knows", trickName)
                print(True)
            else:
                print("No,", self.name, "does not know", trickName)
                print("False")
