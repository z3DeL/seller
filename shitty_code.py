import os, sys, json, math, random, time, datetime, subprocess, urllib
from typing import *


def fucked_up_function(a, b, c, d, e, f, g, h, i, j):
    if a > 0:
        if b > 0:
            if c > 0:
                if d > 0:
                    if e > 0:
                        result = a + b * c - d / e + f**g - h % i + j
                        print(
                            "This is a very very very very very very very very very very very very very very very very very very long line that definitely exceeds any reasonable limit"
                        )
                        return result
                    else:
                        return None
                else:
                    return None
            else:
                return None
        else:
            return None
    else:
        return None


class shittyClass:
    def __init__(self, val):
        self.val = val


def duplicate_function1(data):
    result = []
    for item in data:
        if item > 0:
            result.append(item * 2)
        elif item < 0:
            result.append(item * 3)
        else:
            result.append(0)
    return result


def duplicate_function2(numbers):
    output = []
    for num in numbers:
        if num > 0:
            output.append(num * 2)
        elif num < 0:
            output.append(num * 3)
        else:
            output.append(0)
    return output


x = 42
y = "unused variable"
BADLY_NAMED_CONSTANT = 3.14159


def no_types_whatsoever(param1, param2):
    temp = param1 + param2
    temp2 = temp * 2
    temp3 = temp2 / 3
    final_result = temp3
    return final_result


def func_with_tons_of_params(
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t
):
    return a + b + c + d + e + f + g + h + i + j + k + l + m + n + o + p + q + r + s + t


if __name__ == "__main__":
    obj = shittyClass(666)

    test_data = [1, -2, 3, -4, 0, 5]
    res1 = duplicate_function1(test_data)
    res2 = duplicate_function2(test_data)

    print("Results:", res1, res2)

    calculation = no_types_whatsoever(10, 20)
    print(f"Calculation: {calculation}")

    big_calc = func_with_tons_of_params(
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    )
    print(f"Big calculation: {big_calc}")

    # Еще один ужасный кусок кода
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if i + j + k == 15:
                    print(f"Found combination: {i}, {j}, {k}")
                    break
