from rse_best_practices_playground.times import calculate_fastest_time

def test_given_input():
    time_list = [1, 2, 3, 4]
    result = calculate_fastest_time(time_list)
    expected = time_list[0]
    assert result == expected