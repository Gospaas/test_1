def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

def sort_list(lst):
    return sorted(lst)

seq = input("Введите последовательность чисел через пробел: ").split()
try:
    seq = [int(num) for num in seq]
except ValueError:
    print("Ошибка: последовательность должна состоять только из чисел!")
    exit()

target = input("Введите число: ")
try:
    target = int(target)
except ValueError:
    print("Ошибка: введено некорректное число!")
    exit()

sorted_seq = sort_list(seq)
pos = binary_search(sorted_seq, target)

if pos == len(sorted_seq):
    print("Введенное число больше всех чисел в последовательности")
elif pos == 0 and sorted_seq[0] > target:
    print("Введенное число меньше всех чисел в последовательности")
else:
    print(f"Номер позиции элемента, который меньше введенного числа, а следующий за ним больше или равен этому числу: {pos}")
