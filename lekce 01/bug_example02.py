# Výpočet aritmetického průměru.

def average(lst):
    value = 0
    count = 0

    for x in lst:
        value += x
        count += 1

    return value / count

# Problémy:
# - pro prázdný seznam vyhodí neošetřenou výjimku z důvodu dělení nulou
# - zbytečné „znovuvynalézání kola“ namísto použití vestavěných funkcí

# Doporučené řešení:

def average(lst):
    try:
        return sum(lst) / len(lst)
    except ZeroDivisionError:
        return None
