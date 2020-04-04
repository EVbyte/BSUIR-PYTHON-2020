import unittest
from abc import ABC, abstractmethod


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

    def __init__(self, obj):
        self.obj = obj

    def to_json(self):
        return self.surealism(self.obj)

    def surealism(self, obj):

        json_string = ''

        if isinstance(obj, int):
            if obj is True:
                return 'true'
            elif obj is False:
                return 'false'
            else:
                return str(obj)
        elif obj is None:
            return 'null'
        elif isinstance(obj, str):
            return '"{}"'.format(obj)
        elif isinstance(obj, list):
            json_string += '['
            for element in obj:
                json_string += self.surealism(element)
                json_string += ', '
            json_string = json_string[0:-2]
            json_string += ']'
            return json_string
        elif isinstance(obj, dict):
            json_string += '{'
            for key, value in obj.items():
                json_string += self.surealism(key)
                json_string += ': '
                json_string += self.surealism(value)
                json_string += ', '
            json_string = json_string[0:-2]
            json_string += '}'
            return json_string
        elif isinstance(obj, tuple):
            json_string += '('
            for element in obj:
                json_string += self.surealism(element)
                json_string += ', '

            json_string = json_string[0:-2]
            json_string += ')'
            return json_string
        else:
            return self.surealism(obj.__dict__)


class TestToJson(unittest.TestCase):
    def setUp(self):
        self.hero = Hero()
        self.berserk = Berserk(self.hero)
        self.temp = JSON(self.berserk.get_stats())
        print(self.temp.to_json())
        self.json_string = '{"HP": 178, "MP": 42, "SP": 100, "Strength": 22, "Perception": 1, "Endurance": 15, "Charisma": -1, "Intelligence": 0, "Agility": 15, "Luck": 8}'

    def test_to_json(self):
        self.assertEqual(self.temp.to_json(), self.json_string)


if __name__ == "__main__":
    hero = Hero()
    berserk = Berserk(hero)
    t = JSON(berserk.get_stats())
    print('JSON str:', t.to_json())
    unittest.main()
