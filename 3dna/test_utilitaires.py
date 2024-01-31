from utilitaires import*
from pytest import*

### BATTERIE DE TEST POUR utilitaires.py ###

### Il suffit de RUN le fichier ###

def test_dec_to_bin():
    assert dec_to_bin(0) == '0'
    assert dec_to_bin(1) == '1'
    assert dec_to_bin(10) == '1010'


def test_bin_to_dec():
    assert bin_to_dec(0) == '0'
    assert bin_to_dec(1) == '1'
    assert bin_to_dec(1010) == '10'

def test_quicksort():
    assert quicksort([0],0,0) == [0]
    assert quicksort([3,2,0,1],0,3) == [0,1,2,3]
    
def test_partition():
    pass

def test_list_to_str():
    pass

def test_decompose_dict_list():
    pass

def test_resize_bin():
    pass

def test_change_str():
    pass

def test_merge_dict():
    pass

def test_back_to_dec():
    pass

