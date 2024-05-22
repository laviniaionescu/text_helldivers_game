import weapons


class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
        self.max_health = health

        self.weapon = weapons.rifle

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        print(f"{self.name} dealt {self.weapon.damage} damage to {target.name} with {self.weapon.name}")


class Helldiver(Character):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name=name, health=health)

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped a {self.weapon.name}")


class Boss(Character):
    def __init__(self, name: str, health: int, weapon) -> None:
        super().__init__(name=name, health=health)
        self.weapon = weapons.titan_attack
