class Weapon:
    def __init__(self, name: str, damage: int) ->None:
        self.name = name
        self.damage = damage


auto_cannon = Weapon(name="Auto Cannon", damage=10)

anti_tank = Weapon(name="Anti Tank RPG", damage=20)

railgun = Weapon(name="Railgun", damage=15)

rifle = Weapon(name="Rifle", damage=5)


titan_attack = Weapon(name="Bile", damage=15)