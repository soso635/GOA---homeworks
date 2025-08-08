# 1) მომხმარებელს შემოატანინეთ სიტყვა, თუ ამ სიტყვის სიგრძე არის 5-ზე მეტი, მაშინ გამოვიტანოთ ყველა ასო, პატარა შრიფტით, თუ არადა დიდით.

text = input("enter word: ")

if len(text) >= 5:
    print(text.lower())
else:
    print(text.upper())



#2)შექმენით ფუნქცია რომელიც არგუმენტად იღებს სიტყვას/წინადადებას და ასოს, ის აბრუნებს პირველი სად შეხვდა ასო ამ სიტყვაში


def find_letter(hello, o):
    find =  hello.find(o)
    return find

print(find_letter("hello", "o"))








# 3) შექმენით ერთი ვოიდ ფუნქცია და ერთი ფუნქცია რომელიც აბრუნებს სტრინგს.


def greet(name):
    return "hello" + name

print(greet("soso"))



def greet():
    greet = "soso"
    return greet

print(greet())


