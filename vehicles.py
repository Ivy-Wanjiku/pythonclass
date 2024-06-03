class Vehicle:
    def __init__(self,make,model,colour):
        self.make=make
        self.model=model
        self.colour=colour
    def move(self):
        print("start moving")
    def hoot(hoot):
        print("honk honk")
class Bus(Vehicle):
    def __init__( self,make,model,colour,capacity):
        super().__init__(make,model,colour)
        self.capacity=capacity
    def start_Boarding(self):
        print("The bus is now boarding")
class Lorry(Vehicle):
    def __init__(self,make,model,colour,max_board):
        super().__init__(make,model,colour)
        self.max_board=max_board
    def load(self):
        print("Started loading")