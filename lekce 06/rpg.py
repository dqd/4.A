# Ukázka použití objektově orientovaného programování pro implementaci fantasy RPG (role playing game)


class Inventory:
    """
    Inventář
    """

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def __str__(self):
        if self.items:
            return ", ".join(self.items)

        return "[prázdný]"


class Character:
    """
    Postava
    """

    def __init__(self, name, health, strength, defense):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        # každá postava má svůj inventář
        self.inventory = Inventory()

    def attack(self, other):
        # spočítej poškození způsobené útokem
        damage_dealt = self.strength - other.defense
        other.health -= max(damage_dealt, 0)  # zabrání zápornému zdraví
        return damage_dealt

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        # vrátí řetězec s detaily o postavě včetně inventáře
        return (
            f"{self.name} (zdraví: {self.health}, síla: {self.strength}, "
            f"obrana: {self.defense}, inventář: {self.inventory})"
        )


# třída Warrior dědí z třídy Character
class Warrior(Character):
    """
    Válečník
    """

    def __init__(self, name, health, strength):
        super().__init__(name, health, strength, defense=5)
        self.class_name = "Válečník"

    def block(self):
        # válečníci mají zvláštní schopnost blokovat útoky
        self.defense += 2

    def __str__(self):
        return super().__str__() + f", třída: {self.class_name}"


# třída Mage dědí z třídy Character
class Mage(Character):
    """
    Mág
    """

    def __init__(self, name, health, strength):
        super().__init__(name, health, strength, defense=2)
        self.mana = 100
        self.class_name = "Mág"

    def cast_spell(self, other):
        # mágové mají speciální magický útok
        if self.mana >= 10:
            self.mana -= 10
            # poškození kouzlem ignoruje normální obranu
            spell_damage = self.strength * 2
            other.health -= spell_damage
            return spell_damage

        print("Nedostatek many!")
        return 0

    def __str__(self):
        return super().__str__() + f", mana: {self.mana}, třída: {self.class_name}"


# příklad použití
warrior = Warrior("Aragorn", health=100, strength=15)
mage = Mage("Gandalf", health=80, strength=10)

# přidání předmětů do inventáře postavy
warrior.inventory.add_item("meč")
warrior.inventory.add_item("štít")
mage.inventory.add_item("kouzelnická hůlka")

print(warrior)  # zobrazí detaily válečníka včetně inventáře
print(mage)  # zobrazí detaily mága včetně inventáře

# mág sesílá kouzlo na Válečníka
mage.cast_spell(warrior)
print(warrior)  # zobrazí detaily válečníka včetně aktualizovaného zdraví
