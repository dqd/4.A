# Vypsání všech čísel v jednom řetězci až po "n".

def concatenation(n, result=""):
    if n < 0:
        return result
    else:
        result = concatenation(n - 1, result)
        return result + ', ' + str(n)
