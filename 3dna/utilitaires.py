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
    list = [ch for keys in dict.keys() for ch in str(dict[keys])]
    return list

def resize_bin(binaire_str, n):
    zeros_a_ajouter = '0' * (n - len(binaire_str))
    resultat = zeros_a_ajouter + binaire_str
    return resultat

def change_str(str, n, char):
    nouvelle_chaine = str[:n] + char + str[n+1:]
    return nouvelle_chaine
'''
def merge_dict(dict1, dict2):
    result = {}
    for key in dict1.keys():
        result[key] = list(set(dict1[key] + dict2[key]))
    
    return result
'''
def merge_dict(dict1, dict2):
    result = {}
    for key in set(dict1.keys()) | set(dict2.keys()):
        # If the key is in both dictionaries, merge the values as lists
        if key in dict1 and key in dict2:
            value1 = dict1[key] if isinstance(dict1[key], list) else [dict1[key]]
            value2 = dict2[key] if isinstance(dict2[key], list) else [dict2[key]]
            result[key] = list(set(value1 + value2))
        # If the key is only in one dictionary, use its value
        elif key in dict1:
            result[key] = dict1[key]
        elif key in dict2:
            result[key] = dict2[key]
    return result

def back_to_dec(dict):
    resultat = {}

    for cle, valeur_binaire in dict.items():
        valeur_decimal = int(valeur_binaire.replace('b',''), 2)
        valeur_decimal_divisee = valeur_decimal / 1000
        resultat[cle] = valeur_decimal_divisee

    return resultat

