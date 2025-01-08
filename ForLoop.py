# for loop = fixed no of time garnu xa vane use for loop
#            u can iterate over a range , string, sequence, etc.

for x in range(0, 10, 2 ):
    print(x)

print("happy new year!")

for x in reversed(range(1, 10)):
    print(x)
print("Rocket lunched")

credit_card = "1234-5678-9012-3456"
for x in credit_card:
    print(x)

for x in range(1, 10):
    if x== 5:
        continue  #it remove 5 from list
    else:
        print (x)


for x in range(1, 10):
    if x== 5:
        break  # break break the loop
    else:
        print (x)
