"""
Character Stat Testing
"""


class Character:
    def __init__(self, name: str, strength: int, strength_percent: float):
        self.stats = {"name": "No Name", "strength": 10, "strength_percent": 100}
        if type(name) is str:
            self.stats["name"] = name
        if type(strength) is int:
            self.stats["strength"] = strength
        if type(strength_percent) is float:
            self.stats["strength_percent"] = strength_percent

    def upgrade_stat(self, stat: str, amount_change: int):
        if stat in self.stats:
            prev_stat = self.stats[stat]
            self.stats[stat] = self.stats[stat] + amount_change
            print(f"{self.stats['name']} {stat.capitalize()} Change: {prev_stat} -> {self.stats[stat]}")
        else:
            print(f"Stat '{stat}' doesn't exist")

    def calc_stat(self, stat: str):
        if stat != "name":
            eff_stat = self.stats[stat] * (self.stats[f"{stat}_percent"]/100)
            return eff_stat

    def eff_stat(self, stat: str):
        eff_stat = self.calc_stat(stat)
        print(f'Effective {stat.capitalize()}: {eff_stat:.2f}'
              f'\nBase {stat.capitalize()}: {self.stats[stat]}'
              f'\n{stat.capitalize()} Percentage: {self.stats[f"{stat}_percent"]}%')

    def compare_stat(self, stat, character):
        if self.calc_stat(stat) > character.calc_stat(stat):
            print(f"{self.stats['name']} is stronger than {character.stats['name']}!")
        elif self.calc_stat(stat) == character.calc_stat():
            print(f"{self.stats['name']} has equal strength to {character.stats['name']}!")
        else:
            print(f"{self.stats['name']} is weaker than {character.stats['name']}!")


char = Character('Char1', 20, 125.6)
char2 = Character("Char2", 10, 100)
char.eff_stat("strength")
char.compare_stat("strength", char2)
char.upgrade_stat("strength", 10)
