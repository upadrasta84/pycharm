from MyFirstPythonClass import Dog

my_dog = Dog('lab', '3', 4, False)

print(my_dog)
print(my_dog.breed)

print(my_dog.species)
print(Dog.species) #like a class variable
my_dog.bark()

from MyFirstPythonSubClass import Puppy
my_puppy = Puppy()
my_puppy.bark()
my_puppy.eat()