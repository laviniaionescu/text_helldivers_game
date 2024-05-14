class Character:
    def __init__(self, name: str, health: int, damage: int) -> None:
        self.name = name
        self.health = health
        self.max_health = health
        self.damage = damage

    def attack(self, target) -> None:
        target.health -= self.damage
        target.health = max(target.health, 0)


