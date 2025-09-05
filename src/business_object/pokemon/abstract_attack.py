from abc import ABC, abstractmethod


class AbstractAttack(ABC):
    def __init__(self, power, name, description):
        self._power = power
        self._name = name
        self._description = description

    @abstractmethod
    def compute_damage(self, attacking_pokemon):
        pass

    @property
    def power(self):
        return self._power

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description
