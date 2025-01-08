#object= a "bundle" of related attributes (variables)
# and method(functions)
#  ex. phone, cup, book
#  u need class too create many objects
#  class= (blueprint) used to degine structure & layout of an obj

class Car:
    def __init__(self, model, color, year, for_sale):  # model, color, year, for_sale are attributes
        # assigning attributes
        self.model = model
        self.color = color
        self.year = year
        self.for_sale = for_sale

    # methods
    def drive(self):
        print(f"You drive the car of {self.year}")

    def stop(self):
        print(f"You stopped the {self.color} of {self.model} car")

# Creating car objects
car1 = Car("Mustang", "pink", 2025, True)
car2 = Car("Corvette", "red", 2024, False)

# Print car details
print(car1)  # It will print out the memory address of the car object

# Accessing attributes
print(car1.year)       # Prints: 2025
print(car1.for_sale)   # Prints: True
print(car2.color)      # Prints: red
print(car2.model)      # Prints: Corvette

# Accessing methods
car1.drive()           # Prints: You drive the car of 2025
car1.stop()            # Prints: You stopped the pink car

car2.drive()           # Prints: You drive the car of 2024
car2.stop()            # Prints: You stopped the red car

# These lines below are not needed because the methods already print the output
# print(car1.drive())   # This would return None
# print(car2.stop())    # This would return None


