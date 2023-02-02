# Задача №17.
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6


# print(len(set(input().split())))

from random import randint

# lst = [1, 1, 2, 0, -1, 3, 4, 4]
# # print(lst)
# lst = set(lst)
# print(len(lst))

n = int (input("Введите количество чисел: "))
lst = [randint(-10, 10) for _ in range(n)]
print(lst)
lst = set(lst)
print(len(lst))