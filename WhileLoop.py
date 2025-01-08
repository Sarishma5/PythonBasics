#WHILE LOOP AND WHILE NOT LOOP

name= input ("enter ur name")

while name== "":
  print("did u not enter ur name")
  name= input("enter your name")
  print(f"hello {name}")

age= int(input("enter ur age: "))
while age<0:
  print("age can't be negative")
  age= int(input("enter ur age: "))

  print(f"your age is {age}")

color = input("enter the color u likr(q to quit): ")

while not color== "q":
    print(f"which color u like {color}")
    color= input("enter another color u like(q to quit): ")
    print("bye")


# sent = input("enter a sentance: ")

# while sent:

#   print(f"python is fun")




sent = input("Enter a sentence: ")

while sent != "exit":
    print("Python is fun")
    sent = input("Enter a sentence: ")
    print("enter 'exit' to exit")

print("Loop has stopped.")
  

#Ask the initial question
ans = input("Do you love me? yes or no: ")

while ans != "yes":
    print("Hey, love me 🙄🙄")
    ans = input("Do you love me? No is not allowed, say yes now: ")

print("I love you too, babe ❤❤❤")


