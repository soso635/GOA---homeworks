#dict = {key : value , key2 : value2}

#იწერება კლაკნილი ფრჩხილებით, key და value, ერთმანეთისგან გამოიყოფა ორი წერტილით. ყველა ელემენტი უნდა გამოვყოთ მძიმით. 

# + სწრაფად ეძებს მონაცემებს. მონაცემები ინახევა key და value ფორმატებში, მრავალი სასარგებლო პლიუსი : item, value, keys... მარტივად შეგვიძლია ელემენტების დამატება და წაშლა.

# - key უნდა იყოს უნიკალური, სჭირდება ბევრი მეხსიერება.









# 4) უკვე შექმნილ Dictionary-ში დაამატეთ ელემენტი (თქვენი საყვარელი ფერი.

#1) კომენტარების სახით ახსენით რა არის Dictionary.

#dictionary  არის მონაცემთა ტიპი რომელიც ინფორმაციას ინახავს key და value წყვილის სახით


# 2) შექმენი Dictionary, სადაც შენახული იქნება შენს შესახებ ინფორმაცია (სახელი, ასაკი, გვარი)

me = {
   "name" : "soso",
   "surname" : "khutsishvili",
   "age" : "17"

}




# 3) უკვე შექმნილი Dictionary-დან წამოიღეთ მხოლოდ key-ები და ასევე value.

me = {
   "name" : "soso",
   "surname" : "khutsishvili",
   "age" : "17"

}

print(me.keys())

print(me.values())





# 4) უკვე შექმნილ Dictionary-ში დაამატეთ ელემენტი (თქვენი საყვარელი ფერი.



me = {
   "name" : "soso",
   "surname" : "khutsishvili",
   "age" : "17"

}

me["fav_colour"] = "red"
print(me)





#5) უკვე შექმნილ Dictionary-დან, შეცვალე key ისე, რომ value იგივე დარჩეს და დაბეჭდე Dictionary საბოლოო   სახით (გააკეთეთ pop-ით)


me = {
   "name" : "soso",
   "surname" : "khutsishvili",
   "age" : "17"
}
me["სახელი"] = me.pop("name")

print(me)