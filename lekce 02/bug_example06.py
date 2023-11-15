# Vypsání všech čísel v jednom řetězci až po "n" (oddělených čárkou).


def concatenation(n, result=""):
    if n < 0:
        return result
    else:
        result = concatenation(n - 1, result)
        return result + ", " + str(n)


# Problémy:
# - oddělovač (čárka) se nachází i na začátku vraceného řetězce
# - zbytečné a komplikované použití rekurze pro jednoduchý úkol, který lze řešit efektivněji
# - vyhození výjimky "RecursionError: maximum recursion depth exceeded" pro větší hodnoty

# Doporučené řešení:


def concatenation(n, result=""):
    for i in range(n):
        separator = ", " if i > 0 else ""
        result += separator + str(n)

    return result


# Alternativní řešení pomocí generátorové notace seznamu (list comprehension):
# http://diveintopython3.py.cz/comprehensions.html#listcomprehension


def concatenation(n, result=""):
    return ", ".join([str(i) for i in range(n)])


# Alternativní řešení pomocí funkce `map`:


def concatenation(n, result=""):
    return ", ".join(map(str, range(n)))
