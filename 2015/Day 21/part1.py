import copy
class Equipment:
    def __init__(self, stats):
        self.cost = int(stats[0])
        self.damage = int(stats[1])
        self.armor = int(stats[2])
    def display(self):
        print("Cost: {}\nDamage: {}\nArmor: {}\n".format(self.cost, self.damage, self.armor))


class Player:
    def __init__(self):
        self.cost = 0
        self.damage = 0
        self.armor = 0
        self.hp = 100
    def add_item(self, item):
        self.cost += item.cost
        self.damage += item.damage
        self.armor += item.armor
class Boss:
    def __init__(self):
        self.hp = 104
        self.damage = 8
        self.armor = 1
    def display(self):
        print("Boss HP: {}\nBoss damage:{}\nBoss armor: {}".format(self.hp, self.dmg, self.armor))
def fight(player, boss):
    php = player.hp
    pat = player.damage - boss.armor
    if pat < 1:
        pat = 1
    bhp = boss.hp
    bat = boss.damage - player.armor
    if bat < 1:
        bat = 1
    while bhp > 0 and php > 0:
        bhp -= pat
        if bhp < 1:
            return True
        php -= bat
    return False
inputf = open("input.txt", "r")
items = inputf.read().split("\n\n")
weapons = [Equipment([0,0,0])]
armors = [Equipment([0,0,0])]
rings = [Equipment([0,0,0])]
for weapon in items[0].split("\n"):
    weapons.append(Equipment(weapon.split()[1:]))

for armor in items[1].split("\n"):
    armors.append(Equipment(armor.split()[1:]))

for ring in items[2].split("\n"):
    rings.append(Equipment(ring.split()[2:]))
min_cost = float("inf")
max_cost = float("-inf")
for i in range(1, len(weapons)):
    for j in range(0, len(armors)):
        for k in range(0, len(rings)):
            for l in range(0, len(rings)+1):
                player = Player()
                boss = Boss()
                player.add_item(weapons[i])
                player.add_item(armors[j])
                player.add_item(rings[k])
                if l < len(rings) and l != k:
                    player.add_item(rings[l])
                if fight(player, boss):
                    if player.cost < min_cost:
                        min_cost = player.cost
                else:
                    if player.cost > max_cost:
                        max_cost = player.cost
print("Minimum: {}\nMaximum: {}".format(min_cost, max_cost))
