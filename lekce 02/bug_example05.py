# Nalezení prvku v seznamu a vrácení pozice, na které se nachází.


def find_index(lst, value):
    index = 0

    while lst[index] != value:
        index += 1

    return index


# Problémy:
# - neošetřený případ, kdy se prvek `value` nenachází v seznamu `lst`
# - ruční iterace seznamu namísto využití zabudovaných metod

# Doporučené řešení:


def find_index(lst, value):
    if value in lst:
        return lst.index(value)

    return None


# Alternativní řešení s použitím odchycení výjimky:


def find_index(lst, value):
    try:
        return lst.index(value)
    except ValueError:
        return None
