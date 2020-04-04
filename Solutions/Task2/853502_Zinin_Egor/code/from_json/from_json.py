import unittest
import re
from abc import abstractmethod, ABC


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []

        self.stats = {
            "HP": 128,
            "MP": 42,
            "SP": 100,
            "Strength": 15,
            "Perception": 4,
            "Endurance": 8,
            "Charisma": 2,
            "Intelligence": 3,
            "Agility": 8,
            "Luck": 1

        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(ABC, Hero):
    def __init__(self, base):
        self.base = base

    @abstractmethod
    def get_stats(self):
        pass

    def get_positive_effects(self):
        return self.base.get_positive_effects()

    def get_negative_effects(self):
        return self.base.get_negative_effects()


class AbstractPositive(AbstractEffect):

    def get_positive_effects(self):
        effects = self.base.get_positive_effects()
        effects.append(self.__class__.__name__)
        return effects


class AbstractNegative(AbstractEffect):

    def get_negative_effects(self):
        effects = self.base.get_negative_effects()
        effects.append(self.__class__.__name__)
        return effects


class Berserk(AbstractPositive):

    def get_stats(self):
        stats = self.base.get_stats()
        stats['HP'] += 50
        stats['Strength'] += 7
        stats['Perception'] -= 3
        stats['Endurance'] += 7
        stats['Charisma'] -= 3
        stats['Intelligence'] -= 3
        stats['Agility'] += 7
        stats['Luck'] += 7
        return stats



class JSON:

    def from_json(self, json_string):
        regular_string = re.findall(r'\w+|[{\[\]]', json_string)
        iterator_json_string = iter(regular_string)
        return self.decode(iterator_json_string)

    def decode(self, iterator_string):
        next_symbol = next(iterator_string)
        if next_symbol == "{":
            python_dict = {}
            while True:
                try:
                    key = self.decode(iterator_string)
                    python_dict[key] = self.decode(iterator_string)
                except StopIteration:
                    return python_dict
        elif next_symbol == "[":
            python_list = []
            while True:
                next_list_value = self.decode(iterator_string)
                if next_list_value == ']':
                    return python_list
                else:
                    python_list.append(next_list_value)
        elif next_symbol.isdigit():
            return int(next_symbol)
        elif next_symbol == 'null':
            return None
        elif next_symbol == 'true':
            return True
        elif next_symbol == 'false':
            return False
        else:
            return next_symbol


if __name__ == '__main__':
    hero = Hero()
    berserk = Berserk(hero)
    json_task = JSON()
    print("Python object: ", berserk.__dict__)

    print("Python Object:", type(json_task.from_json('{"HP": 178, "MP": 42, "SP": 100, "Strength": 22, "Perception": 1, "Endurance": 15, "Charisma": -1, "Intelligence": 0, "Agility": 15, "Luck": 8}')))
    #unittest.main()







