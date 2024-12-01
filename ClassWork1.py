import random

rand = random.randint (1,10)

pop = 3

for i in range(pop):
    ans = int(input("Число от 1 - 10: "))

    if rand == ans:
        print("YOU WIN")
        break
    if rand > ans:
        print("більше")
    elif rand < ans:
        print("менше")

    print(f"У вас є {pop - i - 1} попиток.")
else:
    print(f"Програав")
print(f"Число {rand} ")
