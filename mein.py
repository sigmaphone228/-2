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