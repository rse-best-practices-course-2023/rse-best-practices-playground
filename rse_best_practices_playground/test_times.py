import times

def test_calculate_fastest_time():
    time_list = [1, 2, 3, 4]
    print(times.calculate_fastest_time(time_list))
    assert isinstance(times.calculate_fastest_time(time_list), int)
    assert times.calculate_fastest_time(time_list) == 1

test_calculate_fastest_time()