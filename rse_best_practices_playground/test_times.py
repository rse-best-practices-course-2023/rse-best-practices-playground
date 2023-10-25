from rse_best_practices_playground import times
import pytest

def test_calculate_fastest_time():
    test_list = [-1,2,3,4]
    with pytest.raises(ValueError):
        times.calculate_fastest_time(test_list)


