# Přidání/úprava klíče ve slovníku.

def add_to_dict(key, value, data_dict={}):
    data_dict[key] = value
    return data_dict

# Problém:
# - kopírování slovníku `data_dict` mezi jednotlivými voláními funkce (sdílení reference)

# Doporučené řešení:

def add_to_dict(key, value, data_dict=None):
    data_dict = data_dict or {}  # kratší zápis if not data_dict: data_dict = {}
    data_dict[key] = value
    return data_dict
