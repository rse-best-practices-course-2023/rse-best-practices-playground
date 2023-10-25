import pytest 
import rse_best_practices_playground.times as times


def test_given_input():
    time_list = [1, 2, 3, 4]
    result = times.calculate_fastest_time(time_list)
    expected = 1
    assert result == expected