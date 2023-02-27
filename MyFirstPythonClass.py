class Dog:

    species = 'mammal'

    def __init__(self, breed, dog_age, number_of_legs, has_tail):
        self.breed = breed
        self.age = dog_age
        self.legs = number_of_legs
        self.tail = has_tail
        print('Dog Created2')

    def bark(self):
        print("woof!")

    def eat(self):
        print("dog eating!")

class Cat:

    def eat(self):
        print("cat eating!")

    def __str__(self): #this dunder method is similar to overriding toString() method in java.
        return "Cat Object"

    def __len__(self): #this dunder is used for the len() BIF. BIF is short for built in function
        return 20
        
    def __del__(self):
        print('cat deleted')

if __name__ == '__main__':
    my_dog = Dog('lab', '3', 4, False)
    my_cat = Cat()

    for pet in [my_dog, my_cat]: #this is polymorphism. Unlike in java, we dont need dog and cat to inherit from same parent to be able to do this. weird!
        pet.eat()
        print(pet) #because we have __str__ implementation of cat but not dog, we get values accordingly.
        #print(len(pet)) #since dog has no __len__ implementation, it will error out

    print(my_cat)
    del(my_cat) #this will delete the object from the memory . when this is done, the __del__ method will be called on the class
    #print(my_cat) #error
