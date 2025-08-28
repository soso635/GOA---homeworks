#tuple - iwereba mrgval frchxilebshi. sheicavs ramdenime tipis monacems. elementebze wvdoma sheudzlia indexit. sheudzlia qondes duplicatebi. 

# + swrafia listebtan shedarebit. nakleb mexsierebas xarjavs. ufro daculia
# - ar shegvidzlia cvlilebis gaketeba. metodebi nakleboba. sheudzlebelia pirdapir monacemebis ganaxleba. 





#1)შექმენით tuple სახელით fruits სადაც იქნება 5 ხილის სახელი. გამოიტანეთ ირველი ელემენტი ბოლო ელემნტი შუა ელემენტი.


fruits = ("ვაშლი", "მარწყვი", "კივი", "ატამი", "ანანასი")

print(fruits[0])
print(fruits[2])
print(fruits[4])




#2)შექმენით Tuple -ი და სეცვალეთ მეორე ინდექსზე მყოფი ელემენტი ზუსტად ისე როგორც გაკვეთილზე განახეთ, სბოლოოდ გამოპრინტეთ ახალი tuple ელემენტ შეცვლილი. ახსენით კომენტარებით რომელ ხაზზე რა ხდება.






#3) გააერთიანეთ tuple დაწერეთ ორი tuple და გააერთიანეთ და დაბურნეთ გაერთიანება ასევე გააკეთეთ ერთერთი tuple ის გამრავლება სასურველ რიცხვზე.
t = (1, 2, 3)
t1 = (4, 5, 6)

print(t + t1)
print(t * 7)






#4) შექმენი tuple (1,2,3,4,5,6,6,6,67,8) დაწერეთ რამდენჯერ გვხვდება 6 იანი  და რომელ ინდექსზეა 67-ი.

tuple = (1,2,3,4,5,6,6,6,67,8)

print(tuple.count(6))
print(tuple.index(67))