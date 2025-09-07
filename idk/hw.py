products = {
    "apple": 3,
    "banana": 2,
    "milk": 5
}

# მომხმარებლისგან პროდუქტის შეყვანა
item = input("Enter product name: ")

# ვამოწმებთ არსებობს თუ არა
if item in products:
    print(f"{item} costs {products[item]}")
else:
    print("This product is not available.")
