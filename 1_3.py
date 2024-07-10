import pytest

def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    return b ** 2 - 4 * a * c

def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    d = discriminant(a, b, c)
    if d < 0:
        return "корней нет"
    elif d == 0:
        x = -(b / (2 * a))
        return x
    else:
        x_1 = -(b + d ** 0.5) / (2 * a)
        x_2 = -(b - d ** 0.5) / (2 * a)
        return x_2, x_1

def test_discriminant():
    assert discriminant(1, 8, 15) == 4
    assert discriminant(1, -13, 12) == 121
    assert discriminant(-4, 28, -49) == 0
    assert discriminant(1, 1, 1) == -3

def test_solution():
    assert solution(1, 8, 15) == (-3.0, -5.0)
    assert solution(1, -13, 12) == (12.0, 1.0)
    assert solution(-4, 28, -49) == 3.5
    assert solution(1, 1, 1) == "корней нет"
