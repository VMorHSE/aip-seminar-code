# Написать положительные тесты для функции merge
from merge import merge

def test_merge_two_empty():
    assert merge([], []) == []
    
def test_merge_first_empty():
    assert merge([], [1, 2, 4]) == [1, 2, 4]
   
def test_merge_second_empty():
    assert merge([1, 2, 4], []) == [1, 2, 4]

def test_merge_one_in_first():
    a = [5]
    b = [1,2,3,4,6]
    assert merge(a,b) == [1,2,3,4,5,6]
    
def test_merge_one_in_second():
    a = [5]
    b = [1,2,3,4,6]
    assert merge(b,a) == [1,2,3,4,5,6]
    
def test_merge_one_in_both():
    a = [1]
    b = [2]
    assert merge(a,b) == [1,2]
    
def test_merge_diferent_lenght():
    a=[1,2,5,6,7]
    b=[3,10]
    assert len(merge(a,b) ) == 7
    
def test_merge_1_after_1 ():
    a = [ 1, 3, 5]
    b = [ 2, 4, 6]
    assert merge(a,b) == [1, 2, 3, 4, 5, 6]

def test_merge_secon_after_first():
    a = [1, 2, 3, 4]
    b = [5, 6, 7]
    assert merge(a,b) == [1, 2, 3, 4, 5, 6, 7]
    
def test_merge_first_after_second():
    a = [1, 2, 3, 4]
    b = [5, 6, 7]
    assert merge(b,a) == [1, 2, 3, 4, 5, 6, 7]
    
