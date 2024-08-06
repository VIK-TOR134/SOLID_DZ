from abc import ABC, abstractmethod

# Шаг 1: Создайте абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализуйте конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

# Шаг 3: Модифицируйте класс Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.__class__.__name__.lower()}.")

    def attack(self):
        if self.weapon:
            print(self.weapon.attack())
        else:
            print("Боец безоружен!")

class Monster:
    def __init__(self, name):
        self.name = name

    def defeat(self):
        print(f"{self.name} побежден!")

# Шаг 4: Реализация боя
def battle(fighter, monster):
    fighter.attack()
    monster.defeat()

# Пример использования
if __name__ == "__main__":
    # Создаем бойца и монстра
    fighter = Fighter("Боец")
    monster = Monster("Монстр")

    # Боец выбирает меч и атакует
    sword = Sword()
    fighter.change_weapon(sword)
    battle(fighter, monster)

    # Боец выбирает лук и атакует
    bow = Bow()
    fighter.change_weapon(bow)
    battle(fighter, monster)