#1)მომხმარებელს შემოატანინეთ 3 რიცხვი და გამოიტანეთ მაგ სამი რიცხვის ჯამი 
#2)დაბეჭდეთ რიცხვები 10 - 1 მდე 
#3)დაბეჭდეთ 1- 100 რიცხვი მხოლოდ კენტები 
#4)დაბეჭდეთ ყველა რიცხვი რომელიც 3 ზე უნაშთოდ იყოფა 
#5)იპოვეთ 1 - 100 რიცხვის ჯამი 


#1)


x = input("enter num: ")
y = input("enter num: ")
z= input("enter num: ")





#2)
count = 10

while count < 10:
    count = count - 1
print("nice job")


#3)
for i in range(1, 100, 2):
    print(i)

num = input("num: ")
if int(num) % 3 == 0:
    print("nice")

#5
s = 0
sum=0

n = 100
while s < 100:
    s = s + 1
    sum = sum + s
print(sum)