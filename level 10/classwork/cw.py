#1) შექმენი for loop- რომელიც გამოიტანს 1-100 ჩატვლით რიცხვებს და ასევე კენტია თუ ლუწი ეს რიცხვი.
for i in range (1, 101, 1):
    print(i)

for i in range (1, 101, 2): #kenti
    print(i)


for i in range(2, 101, 2): #luwi
    print(i)




#2) მომხმარებელს შემოატანინეთ რიცხვი და და გამოიტანეთ ეს რიცხვი კენტია თუ ლუწი
x = input("num: ")
if x % 2 == 0:
    print("even")

if x % 2 != 0:
    print("odd")




#3) მომხმარებელს შემოატანინეთ ორი რიცხვი და დაბეჭდეთ 'მეტია' თუ მეორე რიცხვი პირველზე მეტია თუ არადა დაბეჭდეთ  ''ნაკლებია"

x = int(input("enter ur num: "))
y = int(input("enter ur num: "))

if x > y:
    print("greater")

if x< y:
    print("less")



#4) მომხმარებელს შემოატანინეთ ორი რიცხვი და დაბეჭდეთ უფრო მაღალი რიცხვი
x = int(input("enter num: "))
y = int(input("enter num: "))

if x > y:
    print(x)
if y > x:
    print(y)







