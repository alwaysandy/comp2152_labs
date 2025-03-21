class Person:
    def __init__(self, p_name, p_age, p_height):
            self.__p_name = p_name
            self.__p_age = p_age
            self.__p_height = p_height
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
         self.__name = new_name
    
    def __del__():
        print("The garbage collector is automatically destorying to person object")


person1 = Person("Andy", 26, 179)
print("The name of the person is: " + person1.name)

person1.name = "Maziar"
print("The name of the person is: " + person1.name)