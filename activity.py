# A base class for all vehicles. This is our parent class.
class Vehicle:
    def move(self):
        # This is a generic method. It will be overridden by child classes.
        pass

# The Car class inherits from Vehicle.
class Car(Vehicle):
    def move(self):
        # The Car class provides its own unique implementation of 'move'.
        print("The car is driving 🚗.")

# The Plane class also inherits from Vehicle.
class Plane(Vehicle):
    def move(self):
        # The Plane class provides its own unique implementation of 'move'.
        print("The plane is flying ✈️.")

# The Bicycle class also inherits from Vehicle.
class Bicycle(Vehicle):
    def move(self):
        # And so does the Bicycle class.
        print("The bicycle is pedaling 🚴.")

# A function that can accept any object that has a 'move' method.
# This is a key part of polymorphism.
def perform_action(vehicle):
    vehicle.move()

# Create instances of each vehicle type.
my_car = Car()
my_plane = Plane()
my_bicycle = Bicycle()

# Call the function with different object types.
# The 'perform_action' function doesn't need to know the specific type of vehicle.
# It simply calls the 'move()' method, and the correct version is executed.
print("\n--- Polymorphism in Action ---")
perform_action(my_car)
perform_action(my_plane)
perform_action(my_bicycle)