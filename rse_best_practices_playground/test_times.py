from rse_best_practices_playground.times import calculate_fastest_time

def test_fastest_time_output():
    times_list = [1, 2, 3, 4]
    result = calculate_fastest_time(times_list)
    expected = 1
    assert result == expected, "Fastest time is not 1."

def test_fastest_time_edge_empty():
    times_list = []
    result = calculate_fastest_time(times_list)
    expected = "The list of times is empty."
    assert result == expected, "The function calculate_fastest_time cannot handle empty lists."

def test_fastest_time_edge_negative():
    times_list = [1, -5, 6, 7]
    result = calculate_fastest_time(times_list)
    expected = "At least one of the times is negative."
    assert result == expected, "The function calculate_fastest_time cannot handle negative times."