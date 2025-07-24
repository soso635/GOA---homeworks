#1) მომხმარებელს შემოატანეთ ინფუთი სანამ პირველი და ბოლო ასო ინფუთის არ იქნება ხმოვანი


word = input("enter ur word: ")
if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u" and word[len(word)-1] == "a" or word[len(word)-1]  == "e" or word[len(word)-1]  == "i" or word[len(word)-1]  == "o" or word[len(word)-1]  == "u":
    print("nice work")
else:
    print("try again")
