from rse_best_practices_playground.times import calculate_fastest_time


def test_fastest_time_in_a_specific_case():
    result = [1, 2, 3, 4]
    expected = 1
    assert calculate_fastest_time(result) == expected