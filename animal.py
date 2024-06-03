class Animal:
    def make_sound(self):
        pass
    def move(self):
        pass
    def breath(self):
        pass
    def feed(self):
        pass

class Bird(Animal):
    def make_sound(self):
        print("chirp")
    def move(self):
        print("The bird is fyling")
    def breath(self):
        print("Lungs")
    def feed(self):
        print("beak")
class Fish(Animal):
    def make_sound(self):
        print("Click")
    def move(self):
        print("swim")
    def breath(self):
        print("gills")
    def feed(self):
        print("mouth")
class Dog(Animal):
    def make_sound(self):
        print("bark")
    def move(self):
        print("run")
    def breath(self):
        print("lungs")
    def feed(self):
        print("mouth")
      
class Human(Animal):
    def make_sound(self):
        print("Talk")
    def move(self):
        print("walk")
    def breath(self):
        print("lungs")
    def feed(self):
        print("mouth")
    