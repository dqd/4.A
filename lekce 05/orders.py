import csv
from pathlib import Path

# Zjištění počtu a tržby z prodeje jednotlivých artiklů.

path = Path(__file__).parent / Path("orders.csv")

products = {}

with path.open("r", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)

    for row in reader:
        try:
            quantity = int(row[3])
        except ValueError:
            quantity = 0

        try:
            price = float(row[4])
        except ValueError:
            price = 0.0

        if row[1] not in products:
            products[row[1]] = {
                "name": row[2],
                "quantity": 0,
                "price": 0.0,
            }

        products[row[1]]["quantity"] += quantity
        products[row[1]]["price"] += quantity * price

for product in products.values():
    print("{}: {} pcs, {:.2f} €".format(
        product["name"],
        product["quantity"],
        product["price"],
    ))
