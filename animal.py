from abc import ABCMeta,abstractmethod

class animal(metaclass=ABCMeta):
    def __init__(self,name,age) :

        self.name=name
        self.age=age

    @abstractmethod
    def sound (self) :
        pass
    
    @abstractmethod
    def move (self) :
        pass


class dog (animal):
    def sound(self):
        return "waof"
    def move(self):
        return "Run"

class bird (animal):
    def sound(self):
        return "zzzzz"
    def move(self):
        return "fly"

var1=dog("kalb",3)
print(var1.sound())
var2=bird("soso",1)
print(var2.sound())
var1=dog("kalb",3)
print(var1.move())
var2=bird("soso",1)
print(var2.move())
    

