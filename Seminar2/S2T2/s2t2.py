# 2. Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N.
#     *Пример:*
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

print('Программа принимает на вход число N и выдает набор произведений чисел от 1 до N.')

num = int(input('Введите число N:-> '))
# prods = [1]
# # print(prods)
# for i in range(2, n+1):
#     prods.append(prods[i-2]*i)
# print(prods)

# a=1
# for i in range(2, n+1):
#     print(a, end = ', ')
#     a=a*i
# print(a)

# sum = 1
# for _ in range(num):
#     sum *= _ + 1
#     print(sum, end= ' ')

# sum = 1
# print(sum, end=' ')
# for n in range(2, num+1):
#     sum *= n
#     print(sum, end=' ')

#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

n = int(input())
#пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
fact_list = []
factorial = 1
for i in range(1,n+1):
    factorial*=i
    fact_list.append(factorial)
print(fact_list)

