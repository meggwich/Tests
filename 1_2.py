import pytest

def calculate_square(a):
    perimeter = a * 4
    area = a * a
    return perimeter, area

def test_calculate_square():
    a = 6
    expected_perimeter = 24
    expected_area = 36
    result_perimeter, result_area = calculate_square(a)
    assert result_perimeter == expected_perimeter
    assert result_area == expected_area
