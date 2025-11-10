"""You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N."""

import random


def is_even(integers):
    first = integers[0]
    second = integers[1]
    third = integers[2]

    return (
        True
        if (
            (first % 2 == 0 and second % 2 == 0)
            or (first % 2 == 0 and third % 2 == 0)
            or (second % 2 == 0 and third % 2 == 0)
        )
        else False
    )


def find_outlier(integers):
    if is_even(integers):  # если список четных
        for x in integers:
            if x % 2 != 0:
                return x
    else:
        for x in integers:
            if x % 2 == 0:
                return x


# ls = []
# for x in range(20):
#     ls.append((random.randrange(13), random.randrange(13), random.randrange(13)))
# print(ls)

# for z in ls:
#     print(is_even(z))

ints = [2, 4, 0, 100, 4, 11, 2602, 36]
print(find_outlier(ints))

# понять какой список четный или нет (3 числа минимум?)
# из трех чисел любые два четные
# В любом случае тут будут 2из3 либо четные числа, либо нечетные


# если список четный - вернуть нечетное число (и наоборот)
