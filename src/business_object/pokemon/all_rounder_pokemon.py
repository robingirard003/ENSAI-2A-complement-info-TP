from .abstract_pokemon import AbstractPokemon


class AllRounderPokemon(AbstractPokemon):
    def get_pokemon_attack_coef(self) -> float:
        if self._type == "All rounder":
            multiplier = 1 + (self.sp_atk_current + self.sp_def_current) / 200
        return multiplier
