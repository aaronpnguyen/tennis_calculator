from tennis_calculator import calculate_score
import pytest

# Testing mundane scores before deuces/win situations
@pytest.mark.parametrize('game_score, expected', [
    ([0, 1], 'Love - 15'),
    ([0, 2], 'Love - 30'),
    ([0, 3], 'Love - 40'),
    ([1, 0], '15 - Love'),
    ([2, 0], '30 - Love'),
    ([3, 0], '40 - Love'),
])
def test_calculate_score_love(game_score, expected):

    results = calculate_score(game_score)

    assert results == expected


# Check tied scores below 4 points
@pytest.mark.parametrize('tie_score, expected', [
    ([0, 0], 'Love all'),
    ([1, 1], '15 all'),
    ([2, 2], '30 all'),
])
def test_calculate_score_same_points(tie_score, expected):
    results = calculate_score(tie_score)

    assert results == expected


# Check for deuces at 3 or higher points, (tied game above 3)
@pytest.mark.parametrize('deuce_score, expected', [
    ([3, 3], 'Deuces'),
    ([4, 4], 'Deuces'),
    ([10, 10], 'Deuces'),
    ([1000, 1000], 'Deuces'),
])
def test_calculate_score_deuces(deuce_score, expected):
    results = calculate_score(deuce_score)

    assert results == expected


# Check for ad-in
@pytest.mark.parametrize('ad_in_score, expected', [
    ([4, 3], 'Ad-in'),
    ([24, 23], 'Ad-in')
])
def test_calculate_score_ad_in(ad_in_score, expected):
    results = calculate_score(ad_in_score)

    assert results == expected


# Check for ad-out
@pytest.mark.parametrize('ad_out_score, expected', [
    ([3, 4], 'Ad-out'),
    ([23, 24], 'Ad-out')
])
def test_calculate_score_ad_out(ad_out_score, expected):
    results = calculate_score(ad_out_score)

    assert results == expected


@pytest.mark.parametrize('winning_score, expected', [
    ([4, 0], 'Server wins'),
    ([4, 1], 'Server wins'),
    ([4, 2], 'Server wins'),
    ([25, 23], 'Server wins'),
    ([100, 98], 'Server wins')
])
def test_calculate_score_server_wins_mundane(winning_score, expected):
    results = calculate_score(winning_score)

    assert results == expected

# Check for opponent winning possibilities
@pytest.mark.parametrize('winning_score, expected', [
    ([0, 4], 'Opponent wins'),
    ([1, 4], 'Opponent wins'),
    ([2, 4], 'Opponent wins'),
    ([23, 25], 'Opponent wins'),
    ([98, 100], 'Opponent wins')
])
def test_calculate_score_opponent_wins_mundane(winning_score, expected):
    results = calculate_score(winning_score)

    assert results == expected