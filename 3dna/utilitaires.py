import numpy as np

"""
Fonctions utilitaires utilisées principalement dans genetic.py
"""


def dec_to_bin(num):
    """
    Converts decimal number to binary (as a string).

        Parameters:
            num (float or int): A decimal integer or float
        Returns:
            whole_part+'.'+dec_part or whole_part (str): A binary number as a string  
    """
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
    """
    Converts binary number to decimal

        Parameters:
            binary (float or string): A binary number
        Returns:
            whole_dec+dec_dec (float): Decimal form of binary (as a float)
    """
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

#
def list_to_str(liste):
    """
    Returns a string concatenating each element of the input list.

        Parameters:
            liste (list): A list
        Returns:
            entier (str): String of all concatenated elements of liste
    """
    entier = ''.join(map(str, liste))
    return entier

def decompose_dict_list(dict):
    """
    Returns a list of each character/number of each value (string or integer) of the input dict

        Parameters:
            dict (Dict): A dictionnary whose values are strings or integers
        Returns:
            list (List): A list
    """
    list = [int(ch) for keys in dict.keys() for ch in str(dict[keys])]
    return list

def resize_bin(binaire_str, n):
    """
    Resize binary number to a n-bit binary number

        Parameters:
            binaire_str (str): A binary number
            n (int): Number of bits for binaire_str to be resized
        Returns:
            resultat (str): n-bit binary number (as a string)
    """
    zeros_a_ajouter = '0' * (n - len(binaire_str))
    resultat = zeros_a_ajouter + binaire_str
    return resultat

def change_str(str, n, char):
    """
    Replace the n-th character of str by char

        Parameters:
            str (str): A string
            n (int): An integer
            char (str): A size 1 string
        Returns:
            nouvelle_chaine (str): The modified string

    """
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
    """
    Returns the merged dict of dict1 and dict2 (union of both keys + values of common keys becoming a list)

        Parameters:
            dict1 (Dict): A dictionnary
            dict2 (Dict): Another dictionnary
        Returns:
            result (Dict): The merged dictionnary of dict1 and dict2
    """
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
    """
    Converts a dictionnary's (binary) values to decimal and divide them by 1000

        Parameters:
            dict (Dict): A dictionnary whose values are binary numbers (as a string)
        Returns:
            resultat (Dict): The converted dictionnary
    """
    resultat = {}

    for cle, valeur_binaire in dict.items():
        valeur_decimal = int(valeur_binaire, 2)
        valeur_decimal_divisee = valeur_decimal / 1000
        resultat[cle] = valeur_decimal_divisee

    return resultat

def ordonner_dictionnaire_par_valeur(dictionnaire):
    # Utiliser la fonction sorted avec une fonction de tri personnalisée
    dictionnaire_ordonne = dict(sorted(dictionnaire.items(), key=lambda x: x[1]))
    return dictionnaire_ordonne