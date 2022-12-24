# 1 Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141    $10^-1 ≤ d ≤10^-10

# Судя по примеру, требуется вывести число π c заданным количеством
# цифр после точки
from math import pi

# Вариант решения 1
# Данный вариант не соответствует выводу в примере, но математически верен
def get_pi_by_round(prec:int):
    return round(pi, prec)
    
# Вариант решения 2
# Данный вариант соответствует выводу (округление вниз/отсечение лишних знаков)
def get_pi_by_string(prec:int):    
    return float(str(pi)[:2+prec])

# Вариант решения 3
# через модуль decimal
def get_pi_by_decimal(prec:int, round_type:str):
    import decimal
    d = '1.' + '0'*prec
    dec = decimal.Decimal
    if round_type == 'normal':
        return float(dec(str(pi)).quantize(dec(d), decimal.ROUND_HALF_UP))
    if round_type == 'down':
        return float(dec(str(pi)).quantize(dec(d), decimal.ROUND_DOWN))

def main():

    print('Программа выводит число Пи c указанной точностью')
# Принимаем ввод от пользователя
    s = input('Введите точность (0.1 - 0.0000000001): ')
    if 0.0000000001 <= float(s) <= 0.1:
        d = len(s.split('.')[1])
    else:
        print ("Число вне допуска!")
        return
    num = get_pi_by_round(d)
    print(num, ' Округление при помощи метода round()')
    num = get_pi_by_string(d)
    print(num, ' "Округление" в меньшую сторону через строки ')
    print('Округление с помощью модуля decimal:')
    num = (get_pi_by_decimal(d, 'normal'))
    print(num, ' - округление в большую сторону, если справа число 5 и более (арифметическое)')
    num = (get_pi_by_decimal(d, 'down'))
    print(num, "Округление в меньшую сторону")

if __name__ == "__main__":
    main()