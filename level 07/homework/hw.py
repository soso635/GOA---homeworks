





#1)დაწერე პროგრამა, რომელიც while ციკლით დაბეჭდავს რიცხვებს 1-დან 10-მდე.

w = 0
while w < 10:
    w = w + 1
    print(w)    
#2)დაწერე პროგრამა, რომელიც დაბეჭდავს რიცხვებს 10-დან 1-მდე.

s = 10
while s > 1:
    s = s - 1
    print(s)



#3)კომენტარებით ახსენი while loop.
#while loop - ის დროს კოდი ეშვება იმდენჯერ რამდენჯერაც მოვითხოვთ. შესაძლოა უსასრულოდაც დავპრინტოთ.



# 4)დაწერე პროგრამა, რომელიც სთხოვს მომხმარებელს პაროლის შეყვანას. სწორი პაროლია "python123". სანამ სწორად არ შეიყვანს, მოთხოვე თავიდან.

password = "python123"

enter_password = input("enter ur pass: ")
while password != enter_password:
    enter_password = input("enter ur pass again: ")

print("access granted")



# 5)მომხმარებელმა უნდა შეიყვანოს რიცხვი n. პროგრამამ while ციკლით უნდა დაითვალოს 1-დან n-მდე რიცხვების ჯამი.

s = 0
sum=0

n = int(input("enter num: "))
while s < n:
    s = s + 1
    sum = sum + s
print(sum)

