# collection = single "variable" use to store multiple values
# list= []ordered and changable. Duplicate OK
# set= {} unorderedand immutable, ADD/REMOVE OK, No Dublicates
# Tuple= () ordered and unchangeable Duplicate Ok , Faster


# List
fruits =["apple", "banana", "coconot", "pineapple", "kiwi", "watermalen"]
print(fruits)
print(fruits[2])
print(fruits[0:3]) #0 to 3
print(fruits[::2]) # scap  1
print(fruits[::-1]) 
print(fruits.index("apple"))
fruits[1]= "kiwi" #changable 
fruits.append("graps")
fruits.insert(2, "jackfruit")
fruits.remove("apple")
fruits.sort()
fruits.reverse()
print(fruits.count("kiwi"))
# fruits.clear()


for fruit in fruits:
    print(fruit)
    #print(fruit, end='  ')
    # print(dir(fruits))
    # help(help(fruits))
    print()

print(len(fruits))
print("apple" in fruits)

#SET
fruits ={"apple", "banana", "coconot", "banana"}
print(fruits)
#print(fruits[2]) # indexing cann't  be done
# print(dir(fruits))
# print(help(fruits))
fruits.add("pineapple")
fruits.remove("apple")
fruits.pop()
fruits.clear()

# TUPLE
fruits =("apple", "banana", "coconot", "banana")
print(fruits)
print(len(fruits))
print("apple" in fruits)
print(fruits.index("apple"))
print(fruits.count("coconot"))