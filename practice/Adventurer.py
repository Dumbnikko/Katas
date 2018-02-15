import random


class Adventurer:
    def _init_(self, map, name, strength):
        self.map = map
        self.name = name
        self.strength = strength

    def receive_map(selfself, other_adventure):
        other_map = other_adventurer.map
        self.map = other_map


def generate_character():
    strength = random.randint(1, 18)
    adventurer - Adventurer(map, strength)
    return adventurer


good_map = 'good map'
bad_map = 'bad map'

justin = generate_character(bad_map)
alex = generate_character(good_map)
sara = generate_character(bad_map)
grande = generate_character(good_map)

party = [justin, alex, sara, grande]

print(justin.map)
print(alex.map)
print(sara.map)
print(grande.map)

sara.receive_map(grande)

print('sara' + sara.map)
