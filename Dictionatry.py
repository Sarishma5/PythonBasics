
# Dictionary= a collection of {"key":"values"}pair
#              order & changeable. no duplicates

items= {"bag": "2000",
        "book": "1000",
        "copy": "100",
        "pincle box": "110"}

print(items)

print(items.get("book"))

items.update({"colors": "80"})
items.update({"copy": "50"})
items.pop("pincle box")
items.popitem()
print(items.items())

print(items.keys())

values= items.values()
print(values)


for item in items:
    print(item)

if items.get("colors"):
    print("this item does exits")
else:
    print("this item doesn't exits")


for key, values  in items.items():
    print(f"{key}: {values}")