import datetime

a = datetime.datetime.now()

b = a.year

c = int(input("Введите вашу дату рождения: "))

d = b - c

print(f"Вам {d} лет.")