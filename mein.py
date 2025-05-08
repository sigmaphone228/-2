name = input(" ім'я: ")
age = int(input(" вік: "))
print(f"Привіт {name}, тобі {age}!")
if age > 18:
    print("Вхід дозволено!")
else:
    print("Вхід заборонено!")

import random
secret_number = random.randint(1, 10)
attempts = 3

while attempts > 0:
    guess = int(input("Вгадай число від 1 до 10: "))
    if guess == secret_number:
        print("Вітаю! Ви вгадали!")
        break
    elif guess > secret_number:
        print("Менше")
    else:
         print("Більше")
    attempts -= 1
    if attempts == 0:
        print(f"Ви програли. Загадане число було {secret_number}")

start = int(input("З якого числа почати: "))
end = int(input("До якого числа виводити: "))

for i in range(start, end + 1):
    print(i)

n = int(input("Введи число: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Факторіал числа {n} = {factorial}")

score = int(input("Введи кількість балів: "))

if 0 <= score <= 49:
    print("Незадовільно.")
elif 50 <= score <= 69:
    print("Задовільно.")
elif 70 <= score <= 89:
    print("Добре.")
elif 90 <= score <= 100:
    print("Відмінно.")
else:
    print("Невірне значення балів.")