"""
Домашнее задание №1
Функции и структуры данных

Pipa M.A.
2022-09-16

"""

def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    <<< [1, 4, 25, 49]
    """
    return list(map(lambda x:x**2, args))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(num):
    if num in (0,1):  # не являются простыми числами
        return False
    div_lst = list(filter(lambda x: num % x ==0 , [i for i in range(2,num)]))
    if len(div_lst)>0:
        return False
    else:
        return True

def filter_numbers(num_list, ftype):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    try:
        if ftype == ODD:
            return list(filter(lambda x: x%2 != 0, num_list))
        elif ftype == EVEN:
            return list(filter(lambda x: x%2 == 0, num_list))
        elif ftype == PRIME:
            return list(filter(is_prime, num_list))
        else:
            raise NameError('Wrong filter param, use default constants')
    except NameError:
        raise

if __name__ == '__main__':
    print('Homework 1')

    '''TESTCASES'''
    # print(power_numbers(1,2,3,4,5))
    # print(is_prime(4))
    # print(filter_numbers([1,2,3,4,6,7,8,9,10], ODD))
    # print(filter_numbers([1, 2, 3, 4, 6, 7, 8, 9, 10], EVEN))
    # print(filter_numbers([1, 2, 3, 4, 6, 7, 8, 9, 10], PRIME))
    # print(filter_numbers([1, 2, 3, 4, 6, 7, 8, 9, 10], 'qwe'))