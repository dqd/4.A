# Otevření a načtení souboru.

def read_file(filename):
    f = open(filename, "r")
    data = f.read()
    return data

# Problém:
# - zapomenuté uzavření souboru pomocí `f.close()`, které může vést k různým nechtěným jevům:
#   - únik paměti (memory leak), kdy dochází postupně ke spotřebování paměti
#   - uzamčení souboru zabraňující další práci s ním
#   - potenciální ztráta dat

# Doporučené řešení za pomocí konstrukce with, která soubor automaticky uzavře:

def read_file(filename):
    with open(filename, "r") as f:
        return f.read()
