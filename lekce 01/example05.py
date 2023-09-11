# Nalezení prvku v seznamu a vrácení pozice, na které se nachází.

def find_index(lst, value):
    index = 0

    while lst[index] != value:
        index += 1

    return index
