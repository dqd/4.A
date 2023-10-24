# Funkce pro převod CamelCase na snake_case a naopak.

def camel_to_snake(s):
    if not s:
        return s

    result = [s[0].lower()]

    for x in s[1:]:
        if x.isupper():
            result.append("_")

        result.append(x.lower())

    return "".join(result)


def snake_to_camel(s):
    return "".join([x.capitalize() for x in s.split("_")])

