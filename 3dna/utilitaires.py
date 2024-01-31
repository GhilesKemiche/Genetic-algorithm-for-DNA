import numpy as np
#
def dec_to_bin(num):
    whole_part = bin(int(num))[2:]
    dec_part = ''
    dec = num - int(num)
    while dec != 0:
        dec *= 2
        if dec >= 1:
            dec_part += '1'
            dec -= 1
        else:
            dec_part += '0'
    if dec_part:
        return whole_part + '.' + dec_part
    else:
        return whole_part
    
def decimal_converter(num):
    while(num>1):
        num /= 10
    return num

def bin_to_dec(binary):
    binary = str(binary)
    whole_str, *dec_str = binary.split('.')

    whole_dec = int(whole_str, 2)
    dec_dec = 0.

    if dec_str:
        for k in range(len(dec_str[0])):
            if(dec_str[0][k] == '1'):
                dec_dec = dec_dec + float(2**(-k-1))
    else:
        dec_dec = 0

    return whole_dec + dec_dec

# Call the function as : quicksort(A,0,len(A)-1)
def quicksort(A, lo, hi):
    if lo >= hi or lo < 0:
        return

    p = partition(A, lo, hi)

    quicksort(A, lo, p - 1)
    quicksort(A, p + 1, hi)

def partition(A, lo, hi):
    pivot = A[hi]
    i = lo - 1

    for j in range(lo,hi):
        if A[j]<=pivot:
            i = i + 1
        A[i], A[j] = A[j], A[i]

    i = i + 1
    A[i], A[hi] = A[hi], A[i]
    return i

#
def list_to_str(liste):
    entier = ''.join(map(str, liste))
    return entier

def decompose_dict_list(dict):
    list = [int(ch) for keys in dict.keys() for ch in str(dict[keys])]
    return list

def resize_bin(binaire_str, n):
    zeros_a_ajouter = '0' * (n - len(binaire_str))
    resultat = zeros_a_ajouter + binaire_str
    return resultat

def change_str(str, n, char):
    nouvelle_chaine = str[:n] + char + str[n+1:]
    return nouvelle_chaine

