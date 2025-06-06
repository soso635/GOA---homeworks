#1) შემოაყვანინეთ მომხმარებელს n რიცხვი და დაპრინტეთ ყველა რიცხვი ნოლიდან n+1-მდე

n = int(input("enter num: "))

for i in range(n):
    print(i)


#2) მომხმარებელს სთხოვე შეიყვანოს თავისი ასაკი და მიუთითოს, აქვს თუ არა სტუდენტური ბარათი.
#შემდეგ:
#თუ ასაკი ნაკლებია 18-ზე ან სტუდენტური ბარათი აქვს → დაბეჭდე "დანაზოგი გაქვს!"
#თუ ასაკი 60 ან მეტია და არ აქვს ბარათი → დაბეჭდე "პენსიონერის ფასდაკლება გაქვს!"
#სხვა შემთხვევაში → "ფასდაკლება არ გეკუთვნით"


age = int(input("enter ur age: "))
student_card = True

if age < 18 or student_card == True:
    print("u get discount")

age = int(input("enter ur age: "))
if age >= 60 and student_card == False:
    print("u have a pensioner discount")

else:
    print("no discount")





#3)მომხმარებელს სთხოვე შეიყვანოს ორი რიცხვი. შემდეგ:
#თუ ორივე რიცხვი დადებითია → დაბეჭდე "ორივე დადებითია"
#თუ მხოლოდ ერთი დადებითია → "მხოლოდ ერთი დადებითი რიცხვია"
#თუ არცერთი არ არის დადებითი → "არცერთი არ არის დადებითი"



x = int(input("enter ur num: "))
y = int(input("enter ur num: "))

if x and y > 0:
    print("both num is positive")

x = int(input("enter ur num: "))
y = int(input("enter ur num: "))

if x or y > 0:
    print("one of them is positive")

x = int(input("enter ur num: "))
y = int(input("enter ur num: "))

if x or y <= 0:
    print("none of them is positive")


#4) მომხმარებელი შეიყვანს ორ რიცხვს და ოპერაციას (+, -, *, /)
#დაბეჭდე შედეგი შესაბამისი მოქმედებით.
#თუ ოპერაცია არასწორია (მაგ 0-ს გაყოფა ან ტექსტი ან უცხო სიმბოლო) → "არასწორი ოპერაცია!"

x = int(input("enter ur num w operations: "))
y = int(input("enter ur num w operations: "))

if x + y == False:
    print("wrong operation")



#5) შეამოწმეთ რესურსებში ჩაგდებული სურათი და მის მიხედვით დაწერეთ კომენტარებად ან პრეზენტაციაში მოქმედედების თანმიმდევრობა და საბოლოო პასუხი, ასევე როგორც ნამდვილი პითონის კოდი (შექმენით a,b,c ცვლადები, შექმენით result_0, result_1, result_2 ცვლადები და შეინახეთ თითოეულში შესაბამისი მნიშვნელობა და გამოპრინტეთ). 
A =True
B =False
C =False

res1 = (A and not B) or (B and not A) #True
res2 = (B and C) and (A or B) #false
res3 = (A and not C) or (B and not A) or (B and not C) #true