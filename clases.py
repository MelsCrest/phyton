#CREACIÓN DE CLASES
class Elevator:
    def __init__(self, starting_floor): #_init_ es el constructor
        self.make = "The elevator company"
        self.floor = starting_floor

# To create the object

elevator = Elevator(1)
print(elevator.make) # "The Elevator company"
print(elevator.floor) # 1
