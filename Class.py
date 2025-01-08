
#class & objects 
class House:

     def __init__(self, room, color, flat, place):
        self.room= room
        self.color= color
        self.flat= flat
        self.place= place


     def live(self):
        print("we live in this " +self.color+ " house")

     def leave(self):
        print("we leave this " +str(self.flat)+" house")

        #object
House_1 = House(12, "blue", 4, "kathmandu")
House_2 = House(16, "pink", 5, "Pokhara")

# Accessing attributes
print(House_1.room)
print(House_1.color)
print(House_1.flat)
print(House_1.place)

print(House_2.room)
print(House_2.color)
print(House_2.flat)
print(House_2.place)

# Calling methods
House_1.live()
House_1.leave()

House_2.live()
House_2.leave()

