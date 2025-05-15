#2) კომენტარებით ახსენით რა არის sequences, iteration და selection. მოიყვანეთ მათი მაგალითები

#sequence = თანმიმდევრობა
#iteration = გამეორება
#selection = არჩევანი



#3) კომენტარებით ახსენით, რა არის ალგორითმი და ჩამოთვალეთ რა გზები არსებობს მის წარმოსადგენად.

#ნებისმიერი რამ
#მაგ: კომპიუტერმა დამიბეჭდოს რაიმე კოდი



#4) შეეცადეთ თქვენით მიხვდეთ, თუ რა პასუხს გამოიტანს შემდეგი კოდი:

#print(True or False and False or True and False or False and False or False and True and False or True)-True
#print(5 > 10 or 7 * 7 / 7 == 7 and False or True and "1234" != "1234" and 7 + 3 * 3 + 1 == 15 and True and True or 100 > 100 or True) True
#პირველ რიგში დაუყევით and ლოგიკურ ოპერატორებს, შემდეგ კი დარჩენილ or ოპერატორებს




#5) მომხმარებელს შემოატანინეთ რიცხვი და თუ ის არის ლუწი და არის 10-ზე მეტი, ან ტოლია 7-ის, დაბეჭდეთ True

num = input("enter ur num: ")
if int(num) > 10 or num == 7:
    print(True)
    




#6) ივარჯიშეთ შემდეგ ფუნქციებზე: int, str, float, bool. თითოეულზე გააკეთეთ 3-3 მაგალითი

"soso"
"khutsishvili"
"Tbilisi"

3
44 + 2
53* 7

10.2
3.5
8.9

10>3
True
False



#7) მომხმარებელს შემოატანინეთ წელი და შეამოწმეთ, თუ ის არის ნაკიანი დაბეჭდეთ "This is leap year".(ნაკიანი წელიწადი იყოფა 4-ზე და არ იყოფა 100-ზე ან იყოფა 400-ზე)

year = input("enter year: ")
if int(year) / 4 and int(year)% 100 or int(year) / 400:
    print("This is leap year")


