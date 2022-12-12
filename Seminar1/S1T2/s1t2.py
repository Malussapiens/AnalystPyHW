# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
#  для всех значений предикат.

print('Программа для проверки истинности утверждения')
print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z', end=' ')
print('для всех значений предикат.')
print()
values_xyz = [[0, 0, 0],
              [0, 0, 1],
              [0, 1, 0],
              [0, 1, 1],
              [1, 0, 0],
              [1, 0, 1],
              [1, 1, 0],
              [1, 1, 1]]
print('X', 'Y', 'Z' + '\t'+'¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
for i in range(0, len(values_xyz)):
    x, y, z = values_xyz[i]
    print(x, y, z, end='\t'*2+'    ')
    p1 = not (x or y or z)
    # print(p1, end='\t'+' '*4)
    p2 = not x and not y and not z
    # print(p1, end='\t'*2+' '*4)
    print(p1 == p2)
