# codding: utf-8

name = input ("как вас величать:")
print (name, ",салам алейкум это цирк Монти Пайтона")
answer = input ("Давайте запишемся на курс? (M-массаж R-релакс P-плаванье D-дайвинг)")
if answer == "M" :
    print ("вам окажут комплексный массаж")
elif answer == "R" :
    print ("Курс релаксации с Гейшей")
elif answer =="P" :
    print ("Плаванье в бассейне с инструктором")
elif answer == "D":
    print("Дайвинг с Акулами")
else:
    print("No money,No honey")

