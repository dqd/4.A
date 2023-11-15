# Odstranění sudých čísel ze seznamu.


def remove_even_numbers(lst):
    for num in lst:
        if num % 2 == 0:
            lst.remove(num)

    return lst


# Problém:
# - modifikace seznamu, který je zároveň procházen pomocí cyklu for,
#   což vede k neočekávanému chování

# Ukázka problémového vstupu:
# >>> remove_even_numbers([2, 4, 6, 8])
# [4, 8]

# Doporučené řešení, které prochází kopii seznamu:


def remove_even_numbers(lst):
    for num in lst.copy():  # `lst.copy()` lze nahradit za `list(lst)`
        if num % 2 == 0:
            lst.remove(num)

    return lst


# Alternativní řešení pomocí generátorové notace seznamu (list comprehension):
# http://diveintopython3.py.cz/comprehensions.html#listcomprehension
def remove_even_numbers(lst):
    return [num for num in lst if num % 2 != 0]


# Alternativní řešení pomocí odfiltrování nechtěných prvků:


def remove_even_numbers(lst):
    return list(filter(lambda num: num % 2 != 0, lst))


# Poznámka: výraz `lambda num: num % 2 != 0` je totéž co nově definovaná pomocná funkce, např.:
# def is_odd(num):
#     return num % 2 != 0
# Tu bychom poté ve filtru použili takto:
# `filter(is_odd, lst)`
