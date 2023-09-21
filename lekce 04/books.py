import json

# Zjištění průměrného věku knih v souboru books.json.

with open("books.json", "r") as f:
    content = json.load(f)

books = content.get("books", [])

years = []

for book in books:
    if year := book["year_published"]:
        years.append(year)

print(sum(years) // len(years))
