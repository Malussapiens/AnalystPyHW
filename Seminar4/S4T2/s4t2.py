# 2 Задайте натуральное число N. Напишите программу, которая
#     составит список простых множителей числа N.


def get_prime_divs(num: int):    # возвращает список простых делителей числа num
    from math import ceil
    prime_divs = []
    for i in range(2, ceil(num**0.5 + 0.5) + 1):
        while num % i == 0:
            prime_divs.append(i)
            num //= i
    if num != 1:
        prime_divs.append(num)
    return prime_divs


def main():
    from os import system

    system("cls")
    print('Программа выводит список простых множителей натурального числа N.')
    n = int(input('Введите N: '))
    if n <= 0:
        print('Число не натуральное!')
        return
    if n < 2:
        print('Число не раскладывается на простые множители!')
        return
    print(*get_prime_divs(n))


if __name__ == '__main__':
    main()
