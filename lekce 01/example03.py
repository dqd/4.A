# Odstranění sudých čísel ze seznamu.

def remove_even_numbers(lst):
    for num in lst:
        if num % 2 == 0:
            lst.remove(num)

    return lst
