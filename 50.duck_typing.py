# Duck typing   =   concept where the class of an object is less important than the methods
#                   class type is not checked if minimum methods/attributes are present

class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is qwuacking")

class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person():
    def catch(self,item):
        item.walk()
        item.talk()
        print("You caught the critter")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)

person.catch(chicken)