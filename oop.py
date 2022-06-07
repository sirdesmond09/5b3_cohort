class Dog:
    
    #defining some class attributes.
    species = "Canis familiaris"
    num_of_dogs = 0
    dog_ages = []
    

    #The constructor: This is the initiaization method that is used to define the attributes of the instance.
    def __init__(self, name:str, age:int):
        self.name = name
        
        if not isinstance(age, int):
            raise TypeError("Expected type of age to be int")
        
        self.age = age
        
        Dog.num_of_dogs+=1
        Dog.dog_ages.append(self.age)

    #A string representation method. Tells the computer what to print when you print the class instance without calling anything.
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    #An instance method that takes in another parameter. Instance methods make use of instance attributes and they work differently for each instance but they do the same thing.
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
    
    #A private class method. To create a private method, you need to put a double underscore __ in front of the method. Either instance or class method.
    @classmethod
    def __average(cls):
        return round(sum(cls.dog_ages)/cls.num_of_dogs, 2)
    
    #A class method. 
    @classmethod
    def info(cls):
        return f"I am of {cls.species} and we are {cls.num_of_dogs} in number. The average age of all of us is {cls.__average()}"
        
        
a = Dog("Jack", 3)
a = Dog("Jack", 1)
a = Dog("Jack", 5)
a = Dog("Jack", 6)
a = Dog("Jack", 2)
a = Dog("Jack", 7)
a = Dog("Jack", 9)

print(a)
