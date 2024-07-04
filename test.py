import random
import pytest

def test_roll_dice():
    dice_rolls = roll_dice(5)
    assert len(dice_rolls) == 5
    for roll in dice_rolls:
        assert 1 <= roll <= 6
def test_count_dice_types():
    dice = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4]
    people, cows, chickens, death_rays = count_dice_types(dice)
    assert people == 2
    assert cows == 2
    assert chickens == 2
    assert death_rays == 2
def test_calculate_score():
    assert calculate_score(2, 1, 0) == 3
    assert calculate_score(0, 0, 3) == 3
    assert calculate_score(1, 1, 1) == 6
def test_play_round_lose(player):
    dice = [5, 5, 5, 4]
    play_round(player, dice)
    assert player.score == 0
    assert player.tanks == 3
    assert player.death_rays == 1
def test_play_round_win(player):
    dice = [1, 2, 3, 4, 4, 5, 5]
    play_round(player, dice)
    assert player.score == 6
    assert player.tanks == 2
    assert player.death_rays == 2