#!/usr/bin/env python3

class Dog:
    # Class body goes here

    #Instance method definition
    def bark(self):
        print("Woof!")
    def sit(self):
        print("The dog is sitting.")    

#First Dog instance
bosco=Dog()
bosco.bark()
#Second Dog instance
snoopy=Dog()
snoopy.bark()
snoopy.sit()