# 2 Задайте натуральное число N. Напишите программу, которая 
#     составит список простых множителей числа N.

def get_prime(num:int):    # возвращает ряд положительных простых чисел от 2 до num (алгоритм Эратосфена)
    list_prime = []
    if num < 2:
        return -1
    list_prime.append(2)
    if num > 2:
        for n in range(3, num + 1, 2):
            list_prime.append(n)
    i = 1
    while i < len(list_prime):
        for j in range(3, int(list_prime[i]**0.5 + 1)):
            if list_prime[i] % j == 0:
                del list_prime[i]
                i -= 1
                break
        i += 1
    return list_prime

def get_prime_divs(num:int):    # возвращает список простых делителей числа num
    primes = get_prime(num)
    prime_divs = []
    if not primes:
        return -1
    if num in primes:
        prime_divs.append(num)
        return prime_divs
    while num > 1:
        for i in primes:
            if num % i == 0:
                prime_divs.append(i)
                break
        num /= i
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