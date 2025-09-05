from business_object.pokemon.defender_pokemon import DefenderPokemon
from business_object.statistic import Statistic


class TestDefenderPokemon:
    def test_get_coef_damage_type(self):
        # GIVEN
        snorlax = DefenderPokemon(
            stat_current=Statistic(attack=100, defense=100),
            stat_max=Statistic(attack=100, defense=100, hp=200, sp_atk=50, sp_def=50, speed=30),
            name="Snorlax",
            type_pk="Defender",
        )

        # WHEN
        multiplier = snorlax.get_pokemon_attack_coef()

        # THEN
        assert multiplier == 2


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
