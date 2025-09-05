from business_object.pokemon.attacker_pokemon import AttackerPokemon
from business_object.statistic import Statistic


class TestAttackerPokemon:
    def test_get_coef_damage_type(self):
        # GIVEN
        charizard = AttackerPokemon(
            stat_current=Statistic(attack=100, speed=100),
            stat_max=Statistic(attack=100, defense=80, hp=180, sp_atk=90, sp_def=70, speed=100),
            name="Charizard",
            type_pk="Attacker",
        )
        pikachu = AttackerPokemon(
            stat_current=Statistic(speed=500), name="Pikachu", type_pk="Attacker"
        )

        # WHEN
        charizard_multiplier = charizard.get_pokemon_attack_coef()
        pikachu_multiplier = pikachu.get_pokemon_attack_coef()

        # THEN
        assert charizard_multiplier == 2
        assert pikachu_multiplier == 3.5


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
