from merge import merge

def test_merge_first_empty_list():
    assert merge([], [1,2]) == [1,2]

def test_merge_second_empty_list():
    assert merge([1,2], []) == [1,2]

def test_two_empty_list():
    assert merge([], []) == []

def test_len_merge_list():
    for le in range(1, 11):
        sp1 = range(1, le, 2)
        sp2 = range(2, le, 2)
        
        assert len(merge(sp1, sp2)) == len(sp1)+len(sp2)
