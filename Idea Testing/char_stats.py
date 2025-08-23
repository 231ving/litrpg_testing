"""
Character Stat Testing
"""


class Character:
    def __init__(self, name: str, strength: int, strength_percent: float):
        self.base_stats = {"name": "No Name", "level": 1, "strength": 10, "strength_percent": 100}
        self.modifiers = [{"stat": "strength", "value": 10, "source": "CharPerk"},
                          {"stat": "strength", "value": 10, "source": "CharPerk"},
                          {"stat": "strength_percent", "value": 10, "source": "ItemPerk"}]
        if type(name) is str:
            self.base_stats["name"] = name
        if type(strength) is int:
            self.base_stats["strength"] = strength
        if type(strength_percent) is float:
            self.base_stats["strength_percent"] = strength_percent
        self.modified_stats = self.base_stats.copy()

    def upgrade_base_stat(self, stat: str, amount_change: float):
        if stat in self.base_stats:
            prev_stat = self.base_stats[stat]
            self.base_stats[stat] = self.base_stats[stat] + amount_change
            #print(f"{self.base_stats['name']} {stat.capitalize()} Change: {prev_stat} -> {self.base_stats[stat]}")
        else:
            print(f"Stat '{stat}' doesn't exist")

    def calc_base_stat(self, stat: str):
        if stat != "name":
            eff_stat = self.base_stats[stat] * (self.base_stats[f"{stat}_percent"]/100)
            return eff_stat

    def eff_base_stat(self, stat: str):
        eff_stat = self.calc_base_stat(stat)
        print(f'Effective {stat.capitalize()}: {eff_stat:.2f}'
              f'\tBase {stat.capitalize()}: {self.base_stats[stat]}'
              f'\tBase {stat.capitalize()} Percentage: {self.base_stats[f"{stat}_percent"]}%')

    def compare_base_stat(self, stat, character):
        if self.calc_base_stat(stat) > character.calc_base_stat(stat):
            print(f"{self.base_stats['name']} is stronger than {character.base_stats['name']}!")
        elif self.calc_base_stat(stat) == character.calc_stat():
            print(f"{self.base_stats['name']} has equal strength to {character.base_stats['name']}!")
        else:
            print(f"{self.base_stats['name']} is weaker than {character.base_stats['name']}!")

    def reset_mod_stats(self):
        self.modified_stats = self.base_stats.copy()
        stats = []
        for i in self.modified_stats:
            if i[-len("_percent"):] != "_percent":
                stats.append(i)
                if i not in stats:
                    self.calc_mod_stat(i)
        return None

    def calc_mod_stat(self, stat: str):
        if stat != "name":
            for i in self.modifiers:
                if i["stat"] == stat:
                    self.modified_stats[stat] = self.modified_stats[stat] + i["value"]
                if i["stat"] == f"{stat}_percent":
                    self.modified_stats[f"{stat}_percent"] = self.modified_stats[f"{stat}_percent"] + i["value"]
            mod_stat = self.modified_stats[stat] * (self.modified_stats[f"{stat}_percent"]/100)
            return mod_stat

    def eff_mod_stat(self, stat: str):
        eff_stat = self.calc_mod_stat(stat)
        print(f'Effective {stat.capitalize()}: {eff_stat:.2f}'
              f'\t\tModified {stat.capitalize()}: {self.modified_stats[stat]}'
              f'\t\tModified {stat.capitalize()} Percentage: {self.modified_stats[f"{stat}_percent"]}%')

    def stat_growth_preview(self, level_gain: int, stat: str, base_growth: float, percent_growth: float, interval: int = 1):
        print(f'Level: {self.modified_stats["level"]}', end='\t\t')
        #self.eff_base_stat(stat)
        self.eff_mod_stat(stat)
        for i in range(0, level_gain, interval):
            self.upgrade_base_stat('level', interval)
            self.upgrade_base_stat(stat, base_growth * interval)
            self.upgrade_base_stat(f'{stat}_percent', percent_growth * interval)
            self.reset_mod_stats()
            print(f'Level: {self.modified_stats["level"]}', end='\t\t')
            #self.eff_base_stat(stat)
            self.eff_mod_stat(stat)


char = Character('Char1', 10, 100)
char2 = Character("Char2", 10, 100)

#char.eff_base_stat("strength")
#char.eff_mod_stat("strength")
# char.compare_base_stat("strength", char2)
# char.upgrade_base_stat("strength", 10)

char.stat_growth_preview(1000, 'strength', 2, 0.2, 10)