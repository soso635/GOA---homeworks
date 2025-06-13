# დავალება 1: წნევის ანალიზი
#მომხმარებელი შეიყვანს ორ მაჩვენებელს: სისტოლური და დიასტოლური წნევა.
#პროგრამამ უნდა განსაზღვროს წნევის კატეგორია:

#თუ სისტოლური > 140 ან დიასტოლური > 90 → "მაღალი წნევა"

#თუ სისტოლური < 90 ან დიასტოლური < 60 → "დაბალი წნევა"

#სხვა შემთხვევაში → "წნევა ნორმალურია"


sistoluri_wneva = int(input("enter num: "))
diastoluri_wneva = int(input("enter num: "))

if sistoluri_wneva > 140 or diastoluri_wneva > 90:
    print("წნევა მაღალია")

elif sistoluri_wneva < 90 or diastoluri_wneva < 60:
    print("წნევა დაბალია")
else:
    print("წნევა ნორმალურია")




#დავალება 2: წონის შეფასება ასაკის მიხედვით (უბრალოდ და ლოგიკურად)
# აღწერა:
#მომხმარებელი შეიყვანს საკუთარ ასაკს და წონას.
#პროგრამამ უნდა შეაფასოს წონა ასაკის მიხედვით მარტივი ლოგიკით:

#თუ ასაკი < 10:

#წონა < 20 → "წონა დაბალია"

#წონა 20-40 → "წონა ნორმალურია"

#წონა > 40 → "წონა მაღალია"

#თუ ასაკი 10-17:

#წონა < 40 → "წონა დაბალია"

#წონა 40-65 → "წონა ნორმალურია"

#წონა > 65 → "წონა მაღალია"

#თუ ასაკი 18 ან მეტი:

#წონა < 50 → "წონა დაბალია"

#წონა 50-90 → "წონა ნორმალურია"

#წონა > 90 → "წონა მაღალია"



age = int(input("enter num: "))
weight = int(input("enter num: "))

if age < 10 and weight < 20:
    print("low weight")
elif weight == 20-40:
    print("normal weight")
elif weight > 40:
    print("high weight")

if age == 10 - 17 and weight < 40:
    print("low weight")
elif weight == 40-65:
    print("norm weight")
elif weight > 65:
    print("high weight")

if age >= 18 and weight < 50:
    print("low weight")
elif weight == 50-90:
    print("norm weight")
elif weight > 90:
    print("high weigh")







# დავალება 3: ასაკის შეჯერება დღის მონაკვეთთან
#შეიყვანოს მომხმარებელმა ასაკი და საათი (0-დან 23-მდე). პროგრამამ განსაზღვროს:

#თუ ასაკი < 18 და დრო ≥ 22 → "დროა დაძინების"

#თუ ასაკი ≥ 60 და დრო ≥ 21 → "დასვენება რეკომენდებულია"

#სხვა შემთხვევაში → "შეგიძლიათ გააგრძელოთ აქტივობა"





age = int(input("enter ur age: "))
time = int(input("enter ur time: "))

if age < 18 and time >= 22:
    print("its time to sleep")
elif age >= 60 and time >= 21:
    print("sleep is recommended")
else:
    print("u can continue ur activity")




#დავალება 4: ფიზიკური აქტივობის რეკომენდაცია
# მომხმარებელი შეიყვანს თავის ასაკს და გულის ცემას.
#პროგრამამ უნდა დაარიგოს ასეთი რჩევები:

#ასაკი < 30 და გულისცემა < 140 → "შეგიძლიათ მეტი ივარჯიშოთ"

#ასაკი ≥ 30 და გულისცემა > 170 → "დასვენება გჭირდებათ"

#სხვა შემთხვევაში → "აქტივობის დონე ნორმალურია"


age = int(input("enter ur age: "))
heart_beat = int(input("enter ur heart beat"))

if age < 30 and heart_beat < 140:
    print("u can practice more")
elif age >= 30 and heart_beat > 170:
    print("take a rest")
else:
    print("activity level is normal")



# დავალება 5: ასაკი და კვება
#მომხმარებელი შეიყვანს ასაკს. პროგრამა გასცემს კვების რეკომენდაციას:

#0–12 → "ბევრი ვიტამინიანი საკვები"

#13–25 → "ენერგიის მომცემი საკვები"

#26–59 → "ბალანსირებული რაციონი"

#60+ → "დაბალკალორიული და მსუბუქი საკვები"




age = int(input("enter ur age: "))

if age == 0-12:
    print("ბევრი ვიტამინიანი საკვებია საჭირო")

elif age == 13-25:
    print("ენერგიის მიმცემი საკვები")

elif age == 26-59:
    print("ბალანსირებული რაციონი")
elif age > 60:
    print("დაბალკალორიული და მსუბუქი საკვები")


