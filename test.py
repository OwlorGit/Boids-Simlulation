import random

num_listA = []
for i in range(50):
    number = random.randint(1, 100)
    num_listA.append(number)

print(num_listA)

num_listB = [random.randint(1, 100) for _ in range(50)]
print(num_listB)