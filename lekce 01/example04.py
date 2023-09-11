# Otevření a načtení souboru.

def read_file(filename):
    f = open(filename, "r")
    data = f.read()
    return data
