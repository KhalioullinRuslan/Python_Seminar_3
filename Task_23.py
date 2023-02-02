# Задача №23. 
# Дан список, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов списков, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

from random import randint

n = int (input("Введите число: "))
lst = [randint(-10, 10) for _ in range(n)]
print(lst)
count = 0

for i in range(1, len(lst)):
    if lst[i] > lst[i - 1]:
        count += 1
print(count)