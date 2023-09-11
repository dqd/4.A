# Výpočet aritmetického průměru.

def average(xs):
    value = 0
    count = 0

    for x in xs:
        value += x
        count += 1

    return value / count
