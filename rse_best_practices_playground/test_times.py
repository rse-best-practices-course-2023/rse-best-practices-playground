from .times import calculate_fastest_time

def test_calculate_fastest_time():
    time_list = [1, 2, 3, 4]
    calculate_fastest_time(time_list, print_time=True)
    assert isinstance(calculate_fastest_time(time_list), int)
    assert calculate_fastest_time(time_list) == 1
    assert calculate_fastest_time(time_list, print_time=True) == 1

test_calculate_fastest_time()