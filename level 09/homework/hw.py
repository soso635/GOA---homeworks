#1)ახსენით რა განსხვავებაა implicit და explicit datatype comversion-ში.

#implicit არის როდესაც კომპიუტერი თავისით გარდაქმნის data type - ს.
#explicit არის როდესაც ჩვენი ხელით გარდავქმენით data type.


#2) შექმენით პროგრამა რომელიც მიიღებს მომხარებლისგან input-ს რიხვის სახით და დაბეჭდეთ ამ რიცხვამდე ყველა რიცხვი თანმიმდევრობით. (For loop)


x = int(input("num: "))

for i in range (x + 1):
    print(i)

#3) while loop

x = int(input("num: "))

i = 0
while i <= x:
    print(i)
    i+=1   