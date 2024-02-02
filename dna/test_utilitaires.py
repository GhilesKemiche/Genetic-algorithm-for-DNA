from dna.utilitaires import*
from pytest import*

### BATTERIE DE TEST POUR utilitaires.py ###

### ### RUN python -m pytest  dna/test_utilitaires.py ### ###

def test_dec_to_bin():
    assert dec_to_bin(0) == '0'
    assert dec_to_bin(1) == '1'
    assert dec_to_bin(10) == '1010'


def test_bin_to_dec():
    assert bin_to_dec(0) == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec(1010) == 10

def test_list_to_str():
    assert list_to_str([1,2,3,4,5]) == "12345"
    assert list_to_str([]) == ""
    assert list_to_str(['a','b','c']) == "abc"
    assert list_to_str(['12','34','56']) == "123456"

def test_decompose_dict_list():
    assert decompose_dict_list({'a':123, 'b':456, 'c':789}) == [1,2,3,4,5,6,7,8,9]
    assert decompose_dict_list({'x':'123', 'y':456, 'z':'789'}) == [1,2,3,4,5,6,7,8,9]
    assert decompose_dict_list({}) == []

def test_resize_bin():
    assert resize_bin('101',6) == '000101'
    assert resize_bin('110011',6) == '110011'
    assert resize_bin('1010101',4) == '1010101'

def test_change_str():
    assert change_str("hello",2,"X") == "heXlo"
    assert change_str("Python is great!",6,"-") == "Python-is great!"
    assert change_str("",0,"A") == "A"

def test_merge_dict():
    assert merge_dict({"a": 1, "b": 2, "c": 3},{"d": 4, "e": 5, "f": 6}) == {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}
    assert merge_dict({"a": 1, "b": 2, "c": 3},{"c": 4, "d": 5, "e": 6}) == {"a": 1, "b": 2, "c": [3, 4], "d": 5, "e": 6}
    assert merge_dict({},{"x":10,"y":20,"z":30}) == {"x":10,"y":20,"z":30}

def test_back_to_dec():
    assert back_to_dec({"a": "110", "b": "1010", "c": "11111"}) == {'a': 0.006, 'b': 0.01, 'c': 0.031}
    assert back_to_dec({"x": "101010", "y": "111000", "z": "1001101"}) == {'x': 0.042, 'y': 0.056, 'z': 0.077}

def test_order_dict():
    unsorted_dict = {'b': 2, 'a': 1, 'c': 3}
    assert order_dict(unsorted_dict) == {'a': 1, 'b': 2, 'c': 3}


# On fait appel aux tests
test_dec_to_bin()
test_bin_to_dec()
test_list_to_str()
test_decompose_dict_list()
test_resize_bin()
test_change_str()
test_merge_dict()
test_back_to_dec()
test_order_dict()

