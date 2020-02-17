
# Define an object class named Dog
class Dog:
    def __init__(self, breed, name, weight, age):
        # Define Data Fields for breed, name, weight, and age
        self__breed = breed
        self__name = name
        self__weight = weight
        self__age = age
            
    # Define getters for breed, name, weight, and age
    def getBreed(self):
        return self.__breed

    def getName(self):
        return self.__name

    def getWeight(self):
        return self.__weight

    def getAge(self):
        return self.__age

        
    # Define setters for breed, name, weight, and age
    def setBreed(self, breed):
        self.__breed = breed

    def setName(self, name):
        self.__name = name

    def setWeight(self, weight):
        self.__weight = weight

    def setAge(self, age):
        self.__age = age

