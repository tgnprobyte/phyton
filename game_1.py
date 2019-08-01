import random

words_list = ('автострада', 'бензин', 'инопланетянин',
             'самолет', 'библиотека', 'шайба', 'олимпиада',
             'чемпионат')

secret_word = random.choice(words_list)
print(secret_word)

users_word = ['*'] * len(secret_word)

errors_counter = 0
while True:
   letter = input('введите ОДНУ букву: ').lower()
   if len(letter) != 1 or not letter.isalpha():
       continue

   if letter in secret_word:
       for position, symbol in enumerate(secret_word):
           # print(position, symbol)
           if letter == symbol:
               users_word[position] = letter
       if '*' not in users_word:
           print('\tвы выиграли!!!')
           break
   else:
       errors_counter += 1
       print('\tошибок совершено:', errors_counter)
       if errors_counter == 8:
           print('вы проиграли :(')
           break

   print(''.join(users_word))

print('до встречи')
