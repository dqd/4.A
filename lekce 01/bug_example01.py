# Zjištění, zdali se číslo nachází v daném limitu.


def is_within_limit(n):
    if n < 100:
        return True
    elif n > 100:
        return False


# Problémy:
# - pro číslo 100 funkce neočekávaně vrací None
# - zbytečné větvení podmínek
# - použití magického čísla 100 (namísto pojmenované konstanty)

# Doporučené řešení:

LIMIT = 100


def is_within_limit(n):
    return n < LIMIT
