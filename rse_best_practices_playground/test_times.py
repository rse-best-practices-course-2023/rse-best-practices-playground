from .times import calculate_fastest_time
import pytest
def test_calculate_fastest_time():
    times_list = [0, 1, 2]
    assert calculate_fastest_time(times_list)==0

def test_negative_numbers_raise_error():
    times_list = [-1, 1, 2]
    with pytest.raises(ValueError):
        calculate_fastest_time(times_list)
