from business_object.pokemon.all_rounder_pokemon import AllRounderPokemon
from business_object.statistic import Statistic


class TestAllRouderPokemon:
    def test_get_coef_damage_type(self):
        # GIVEN
        lucario = AllRounderPokemon(
            stat_current=Statistic(sp_atk=100, sp_def=100),
            stat_max=Statistic(attack=90, defense=80, hp=160, sp_atk=100, sp_def=100, speed=90),
            name="Lucario",
            type_pk="All rounder",
        )

        # WHEN
        multiplier = lucario.get_pokemon_attack_coef()

        # THEN
        assert multiplier == 2


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
