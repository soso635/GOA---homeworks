# 1) შექმენი dictionary, სადაც key = სტუდენტის სახელი, value = ქულა.
# შემდეგ loop-ით დაბეჭდე ყველა სტუდენტი და ქულა.

# dictionary (შეგიძლიათ გამოიყენოთ) :
# scores = {
#     "Ana": 95,
#     "Giorgi": 88,
#     "Luka": 76
# }




scores = {
    "Ana": 95,
    "Giorgi": 88,     
     
    "Luka": 76
 }

for scores, names in scores.items():
    print(f"{scores} ქულა {names}")






# 2) უკვე შექმნილ scores dictionary-ში დაამატე ახალი სტუდენტები update()-ით



scores = {
    "Ana": 95,
    "Giorgi": 88,     
     
    "Luka": 76
 }


scores.update({"soso" : 100})
print(scores)




# 3) ამ dictionary-ში:
# countries = {
#     "kay": "Georgia",
#     "fr": "France",
#     "it": "Italy"
# }

# შეცვალე key "kay" → "ge" pop()-ის გამოყენებით.

# დატოვე value უცვლელი.






countries = {
    "kay": "Georgia",
    "fr": "France",
    "it": "Italy"
 }
countries["ge"] = countries.pop("kay") 

print(countries)






# 4) კომენტარების გამოყენებით ახსენი update() ფუნქცია.


#შეგვიძლია ელემენტის ჩამატება


#5) კომენტარების გამოყენებით ახსენით pop() ფუნქცია.

#პოპ ფუნქციით შეგვიძლია ელემენტის ამოღება


# 6) dictionary ფასებით:

# products = {
#     "apple": 3,
#     "banana": 2,
#     "milk": 5
# }


# დაბეჭდე ყველა პროდუქტი for loop-ით.

# მომხმარებლისგან შეიყვანე პროდუქტი, თუ არსებობს → დაბეჭდე ფასი.

# დაამატე ახალი პროდუქტი update()-ით.

# ბოლოს გამოიყენე clear() ჩასაშენებლად, მაგალითად, ცარიელი dictionary-ს დაბეჭდვა დასუფთავების შემდეგ.







products = {
    "apple": 3,
    "banana": 2,
    "milk": 5
}




product = input("enter existing product: ")

if product in products:
    print(f"{product} costs {products[product]} lari")
else:
    print("this product is not in this list")


    #for loop
for products, price in products.items():
    print(f"{products} - ის ფასი {price} ლარი")



    #update
products = {
    "apple": 3,
    "banana": 2,
    "milk": 5
}

products.update({"watermelon" : 1})
print(products)



#clear
products = {
    "apple": 3,
    "banana": 2,
    "milk": 5
}

products.clear()
print(products)