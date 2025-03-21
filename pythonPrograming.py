datas = [12, 3.14, "red", 7, 0.5, "blue", 8.9, 42, "green"]

for i in range(len(datas)):
    if type(datas[i]) == int:
        print(datas[i], "Index", i)

import random

choices = ["rock", "paper", "scissors"]
users = input("سنگ و کاغذ و قیچی  ")
comp = random.choice(choices)
print(f"چیزی که کامپیوتر نوشته {comp}")
if users == comp:
    print("شما مساوی شدید!")
elif (users == "rock" and comp == "scissors") or \
        (users == "paper" and comp == "rock") or \
        (users == "scissors" and comp == "paper"):
    print("شما بردید")
else:
    print("شما باختید")
