import pytest
def get_all_mentors(mentors):
    all_list = []
    for m in mentors:
        all_list += m
    return all_list

def get_all_names(all_list):
    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)
    return all_names_list

def get_unique_names(all_names_list):
    unique_names = set(all_names_list)
    return unique_names

def sort_names(unique_names):
    all_names_sorted = sorted(unique_names)
    return all_names_sorted

# Тесты
def test_get_all_mentors():
    mentors = [["Иван Иванов"], ["Петр Петров"], ["Сидор Сидоров"]]
    assert get_all_mentors(mentors) == ["Иван Иванов", "Петр Петров", "Сидор Сидоров"]

def test_get_all_names():
    all_list = ["Иван Иванов", "Петр Петров", "Сидор Сидоров"]
    assert get_all_names(all_list) == ["Иван", "Петр", "Сидор"]

def test_get_unique_names():
    all_names_list = ["Иван", "Петр", "Сидор", "Иван"]
    assert get_unique_names(all_names_list) == {"Иван", "Петр", "Сидор"}

def test_sort_names():
    unique_names = {"Иван", "Петр", "Сидор"}
    assert sort_names(unique_names) == ["Иван", "Петр", "Сидор"]

pytest.main()