#FUNCTION

def happy_birthday(name, age):
    print(f"Happy birthday to {name}")
    print("Many many happy returns of the day")
    print("Happy happy birthday")
    print(f"You are {age} years old")
    print()

# Function calls
happy_birthday("Sarishma", 21)
happy_birthday("Rohan", 22)
happy_birthday("Diwakar", 19)


  

def display_invoice(uname, amt, due_date):
     print(f"hello {uname}")
     print(f"your bill of  ${amt:.2f} is due: {due_date}")

display_invoice("hari", 200, "nov 5")


#return = stm used to end function ^ send a result back to culler

def add(x, y):
  z= x+y
  return z

def sub(x, y):
  z= x-y
  return z

def mult(x, y):
  z= x*y
  return z

def divide(x, y):
  z= x/y
  return z

print(add(1, 2))
print(sub(5, 8))
print(mult(3, 9))
print(divide(6,7))


def create_name(first, last):
  first= first.capitalize()
  last= last.capitalize()
  return first+ " "+ last

full_name = create_name("sarishma", "regmi")

print(full_name)

