# ТЕСТЫ: Сделать функцию, которая принимает словарь из чисел и строк и возвращает массив длин строк и массив квадратов чисел
from func import func


def test_empty():
    test = {}
    assert func(test) == ([], [])
    
def test_multiple_values():
    test2 = {
        1 : "test",
        2 : "test2",
        3 : "test3"
    }
    assert func(test2) == ([4, 5, 5], [1, 4, 9])
    
def test_empty_strings():
    test3 = {
        1: "",
        2: ""
    }
    assert func(test3) == ([0, 0], [1, 4])
   
    
    