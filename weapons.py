class Weapon:
    def __init__(self, name: str, damage: int) -> None:
        self.name = name
        self.damage = damage


auto_cannon = Weapon(name="Auto Cannon", damage=15)

anti_tank = Weapon(name="Anti Tank RPG", damage=35)

railgun = Weapon(name="Railgun", damage=25)

rifle = Weapon(name="Rifle", damage=5)


titan_attack = Weapon(name="Bile Attack", damage=20)

WEAPONS = """
1. The Auto-Cannon
2. The Anti-Tank
3. The Railgun
"""