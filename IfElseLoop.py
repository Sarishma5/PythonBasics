#if else and elif loop

age=  int(input("enter your age: "))

if age>= 100:
  print("u are too old to sign up")

elif age >= 18:
  print("u r now signed up")

elif age<0:
  print("u havenot been born yet")

else:
  print("u must be 18+ to sign up")


response = input("would u like to hangout with me(y/n): ")

if response == "y":
  print("lets go some where")
  print('where do u like to go')
  place= input()
  print(f"yahu let's go {place}")
elif response== "n":
  print("its okay")


name = input("enter your name")

if name=='':
  print("u didn't type ur name")
else:
  print(f"hello {name}")
  

for_sale = True

if for_sale :
  print("this is for selling")
else:
  print("this is not for sell")
