#დავალება 1:
#შეიყვანე სიტყვა, სანამ მისი პირველი და ბოლო ასოები არ იქნებიან თანხმოვნები.
# რას ნიშნავს?
#შენ უნდა უთხრა რობოტს სიტყვები.
#მაგრამ რობოტი შეგეკითხება ბევრჯერ, სანამ არ ეტყვი ისეთ სიტყვას, რომლის პირველი ასოც და ბოლო ასოც არცერთი არ არის ხმოვანი (ანუ არ არის ა, ე, ი, ო, უ).


# word = input("enter ur word: ")

# #vowel = "aeiou"
# while word[0] in vowel and word[-1] in vowel:
#     word = input("enter ur word again: ")
# else:
#     print("nice job")




#დავალება 2:
#შეიყვანე 5 სიტყვა, მაგრამ შეინახე (დაახსოვრე) მხოლოდ ისინი, რომლებიც სწორია.
 #რა არის „სწორი“ სიტყვა?
#ამაში უნდა გითხრან წინასწარ რა კრიტერიუმით აირჩიე სწორი, მაგრამ დავუშვათ, სიტყვა სწორია მაშინ, როცა მასში ორივე — პირველი და ბოლო ასოები — თანხმოვნებია.

#შენ უნდა უთხრა 5 სიტყვა. რობოტი კი შეინახავს მხოლოდ იმ სიტყვებს, რომლებიც სწორია.
# list = []
# vowels = "aeiou"
# for i in range(5):
#     word = input("enter ur word : ")
#     if word[0] not in vowels and word[-1] not in vowels:
#         list.append(word)
    
       
# print(list)












#დავალება 3:
#რობოტმა უნდა დაითვალოს, რამდენჯერ სცადე სწორი სიტყვის შეყვანა.
#ანუ ყოველ ჯერზე, როცა სწორი სიტყვა უთხარი, უნდა დაიმახსოვროს და უთხრას ბოლოს რიცხვი.

#count = 0
# vowels = "aeiou"
# for i in range(5):
#     word = input("enter ur word : ")
#     if word[0] not in vowels and word[-1] not in vowels:
#        count += 1 
    
       
# print(count)







#დავალება 4:
#შეიყვანე 10 სიტყვა, მაგრამ დაბეჭდოს (გამოაჩინოს) მხოლოდ სწორი სიტყვები.
 #ანუ ისევ იგივე ლოგიკა – 10 სიტყვა უთხარი, მაგრამ ეკრანზე უნდა გამოჩნდეს მხოლოდ სწორი სიტყვები (ისინი, რომელთაც პირველი და ბოლო ასო თანხმოვანია, ან რაც წესია მოცემულ ამოცანაში).

# vowels = "aeiou"
# for i in range(10):
#     word = input("enter ur word: ")
#     if word[0] not in vowels and word[-1] not in vowels:
#         print(word)







#დავალება 5:
#შეიყვანე სიტყვა და რობოტმა უნდა დათვალოს რამდენი ხმოვანია და რამდენი თანხმოვანი აქვს მას.
#გაიმეორებს ამას მანამ, სანამ არ შეიყვან სწორ სიტყვას.

 #ანუ რობოტს ეუბნები სიტყვას → ის გეუბნება:

#"ამ სიტყვაში არის 3 ხმოვანი და 4 თანხმოვანი"

#და გთხოვს ახალს, სანამ სწორ სიტყვას არ ეტყვი. 


word = input("enter ur word: ")
vowelcount = 0
tanxcount = 0
vowel = "aeiou"
while word[0] not in vowel and word[-1] not in vowel:
    
   
    for i in word:
        if i in vowel:
            vowelcount +=1
        else:
            tanxcount +=1
    print(vowelcount)  
    print(tanxcount)   
    word = input("enter ur word again: ")
    if word[0] in vowel and word[-1] in vowel:
        print("incorrect")       
else:
    print("incorrect")


