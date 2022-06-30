import random

spisok = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


my_ticket = [1, 3, 5, 12]
print(f"У вас билет с элементами {my_ticket}.")

count = 1
k = random.sample(spisok, 4)
k.sort()
while my_ticket != k:
    count +=1
    k = random.sample(spisok, 4)
    k.sort()
    print(k)


print(f"Чтобы выиграть, вам потребовалось {count} попыток")

