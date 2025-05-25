#1)მომხმარებელს შემოატანინეთ სამი რიცხვი, start/end/step და ჩასვით for loop-ში სათანადო ადგილას.
start = int(input("enter start num: "))
end = int(input("enter end num: "))
step = int(input("enter step num: "))

for i in range (start, end, step ):
    print(i)



#2მომხმარებელს შემოატანინეთ რიცხვი და დაპრინტეთ რიცხვი ყოველ იტერაციაზე იქამდე, სანამ რიცხვი მომხმარებლის რიცხვს არ გაუტოლდება (While Loop)

x = int(input("enter num: "))

i = 0

while i <= x:
    print(i)
    i+=1



#3)
x = int(input("enter num: "))

for i in range(x+1):
    print(i)