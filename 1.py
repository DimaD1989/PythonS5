# НОД





# a=20
# b=58

# if a < b :
#     a, b = b, a

# while b!=0:
#     a, b = b, a % b

# print(a)
# while a != b:
#     if a > b:
#         a -= b
#     else:
#         b -= a

# print(a)

# def FindMnoj(n):
#     spisok_mnoj = []
#     d = 2
#     while d * d <= n:
#         if n % d == 0:
#             spisok_mnoj.append(d)
#             n //= d
#         else:
#             d += 1
#     if n > 1:
#         spisok_mnoj.append(n)
#     return spisok_mnoj


# n=list(map(int,input('Введите пару чисел через пробел: ').split()))
# n1 = FindMnoj(n[0])
# n2 = FindMnoj(n[1])
# r =[]
# print (n1, n2)
# for i in range(len(n1)):
#     if max(n1) in n2:
#         r.append(max(n1))
#     n1.pop(len(n1)-1)
# print (r)
# res=1
# for i in range(len(r)):
#     res*=r[i]
# print(res)

# Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "plr". 
# То есть, функция должна возвращать True, если такой фрагмент присутствует 
# в строке и False - в противном случае.


# print((lambda x: 'ra' in x)(input()))

# contains = lambda s, sample='ra': sample in s  
# s = input()
# print(contains(s))

# ДЗ3
# nums = list(map(int, input("Задайте список из нескольких чисел через пробел: ").split()))
# odds = []
# sum = 0

# for i in range(1, len(nums), 2):
#     odds.append(nums[i])
#     sum += nums[i]

# my_list = [8, 5, 7, 3, 6]
# print(sum(my_list[1::2]))

# print(f'{nums} -> на нечётных позициях элементы {odds}, ответ: {sum}')

# з2
# import math

# nums = list(map(int, input("Задайте список из нескольких чисел через пробел: ").split()))
# mult = []

# for i in range(math.ceil(len(nums)/2)):
#     mult.append(nums[i] * nums[-i-1])

# print(f'{nums} => {mult}')

# import random

# size = int(input('Введите число: '))
# numeros = []
# couple_product = []
# for i in range (size):
#     numeros.append(random.randint(0,11))
# if size%2==0:    
#     for i in range (size//2):
#         couple_product.append(numeros[i]*numeros[size-1-i])
# else:
#     for i in range (size//2+1):
#         couple_product.append(numeros[i]*numeros[size-1-i])
# print(numeros, '\n', couple_product)

# import random
# b = int(input('Введите кол-во чисел в списке for 2# = '))
# list_b = list(random.randint(0, 10) for i in range(b))
# print(list_b)
# proiz_b = list(list_b[i]*list_b[-1*(1+i)] for i in range(b//2+1*(b%2)))
# print(proiz_b)



# Зд 3
# import math

# list =  [1.7, 1.2, 3.1, 5.3, 10.01]

# min_elem = math.inf
# max_elem = - math.inf

# for i in range(len(list)):
#     if list[i] % 1 < min_elem:
#         min_elem = list[i] % 1
#     elif list[i] % 1 > max_elem:
#         max_elem = list[i] % 1
# print(f'{round(max_elem, 3)} - {round(min_elem, 3)} = {round(max_elem - min_elem, 3)}')

# list = [1.1, 1.2, 3.1, 10.01]
# mix_list = []

# for i in list:
#     mix_list.append(round(i-int(i), 2))

# print(list, end=' => ')
# print(max(mix_list) - min(mix_list))

# Зд4

# a=int(input('Введите число = '))
# print(bin(a))

# a = int(input('введите число для перевода = '))
# b = ''
# while a != 0:
#     b = str(a % 2) + b
#     a = a // 2
# print(b)


# ЗД 5
# N = int(input("Введите целое число: "))
# Fibonacci = [0, 1]
# for i in range(-N, 0):
#     Fibonacci.append((-1) ** (-i + 1) * Fibonacci[-i])
# for i in range(2, N + 1):
#     Fibonacci.append(Fibonacci[i - 1] + Fibonacci[i - 2])
# print(Fibonacci)


# def nega_fibonacci(numb):
#     array = [1, 0, 1]
#     for i in range(1, numb):
#         array.insert(0, array[1] - array[0])
#         array.append(array[-2] + array[-1])
#     return array


# num = int(input('input number: '))
# print(nega_fibonacci(num))


# Задача про Антона
# for i in range(int(input())):
#     s, virus, x  = input(), 'anton', 0
#     for sym in s:
#         if sym == virus[x]:
#             x += 1
#         if x == 5:
#             print(i + 1, end=' ')
#             break


# fridges = ["9", "osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen", "anton", "aoooooooooontooooo", "elelelelelelelelelel", "ntoneeee", "tonee", "253235235a5323352n25235352t253523523235oo235523523523n", "antoooooooooooooooooooooooooooooooooooooooooooooooooooon", "unton"]
# word = 'anton'
# count = 0
# number = 0

# print("Заражены", end = " ")
# for text in fridges:
#     for char in text:
#         if char == word[count]:
#             count += 1
#         if count == len(word):
#             print(f'{number}', end = " ")
#             break
#     number += 1
#     count = 0





