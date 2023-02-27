from MyFirstPythonClass import Dog
class Puppy(Dog): #class puppy is extending from dog
    def __init__(self):
        Dog.__init__(self, 'Alsesion', '4', 4, True)
        print('Puppy Created')


    def eat(self):
        print("puppy eating!")