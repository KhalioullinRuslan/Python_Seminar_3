# Задача №19. 
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

from random import randint
n = int (input("N: "))
k = int (input("K: "))
lst = [randint(-10, 10) for _ in range(n)]
print(lst)
a = 0

for i in range(k):
    # a = lst.pop()
    lst.insert(0, lst.pop())

print(lst)