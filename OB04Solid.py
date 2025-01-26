from abc import ABC, abstractmethod

# Шаг 1: Создаем абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass  # Абстрактный метод, который должен быть реализован в подклассах

# Шаг 2: Реализуем конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."  # Уникальная реализация атаки для меча

class Bow(Weapon):
    def attack(self):
        return "Боец стреляет из лука."  # Уникальная реализация атаки для лука

class Axe(Weapon):
    def attack(self):
        return "Боец рубит топором."  # Уникальная реализация атаки для топора

# Класс Fighter (боец)
class Fighter:
    def __init__(self, name):
        self.name = name  # Имя бойца
        self.weapon = None  # Оружие бойца (изначально отсутствует)

    def change_weapon(self, weapon):
        self.weapon = weapon  # Метод для смены оружия
        print(f"{self.name} выбирает {weapon.__class__.__name__}.")

    def attack(self):
        if self.weapon:
            print(self.weapon.attack())  # Вызов атаки выбранным оружием
        else:
            print(f"{self.name} без оружия и не может атаковать.")

# Класс Monster (монстр)
class Monster:
    def __init__(self, name):
        self.name = name  # Имя монстра

    def defeat(self):
        print(f"{self.name} побежден!")  # Метод, вызываемый при победе над монстром

# Шаг 4: Реализация боя
def battle(fighter, monster):
    print("--- Начало боя ---")
    fighter.attack()  # Боец атакует
    monster.defeat()  # Монстр побежден
    print("--- Конец боя ---\n")

# Основной блок программы
if __name__ == "__main__":
    # Создаем бойца и монстра
    fighter = Fighter("Герой")
    monster = Monster("Злобный Гоблин")

    # Бой с мечом
    fighter.change_weapon(Sword())
    battle(fighter, monster)

    # Бой с луком
    fighter.change_weapon(Bow())
    battle(fighter, monster)

    # Бой с топором
    fighter.change_weapon(Axe())
    battle(fighter, monster)