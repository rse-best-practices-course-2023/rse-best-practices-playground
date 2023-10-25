from .times import calculate_fastest_time


def test_given_input():

    my_level = "beginner"
    time_list = [1, 2, 3, 4]

    print(calculate_fastest_time(time_list))

    result = calculate_fastest_time(time_list)
    expected = 1

    assert result == expected
