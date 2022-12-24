# 3 Задайте последовательность чисел. Напишите программу, которая 
#     выведет список неповторяющихся элементов исходной последовательности.

def get_uniques(nums: list):
    uniques = list()
    for n in nums:
        if nums.count(n) == 1:
            uniques.append(n)
    return uniques

def main():
    from os import system
    
    system("cls")
    print('Программа выведет список неповторяющихся элементов исходной последовательности чисел.')
    s = list(map(int, input('Введите числа через пробел').split()))
    print(get_uniques(s))

if __name__ == '__main__':
    main()