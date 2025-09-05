from .abstract_pokemon import AbstractPokemon


class DefenderPokemon(AbstractPokemon):
    def get_pokemon_attack_coef(self) -> float:
        if self._type == "Defender":
            multiplier = 1 + (self.attack_current + self.defense_current) / 200
        return multiplier
