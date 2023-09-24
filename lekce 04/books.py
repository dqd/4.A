import json
from pathlib import Path

# Zjištění průměrného věku knih v souboru books.json.

# Soubor je umístěn ve stejném adresáři
path = Path(__file__).parent / Path("books.json")

with path.open("r") as f:
    content = json.load(f)

books = content.get("books", [])

years = []

for book in books:
    if year := book["year_published"]:
        years.append(year)

# Výpočet průměrného roku vydání
print(sum(years) // len(years))
