from rse_best_practices_playground.times import calculate_fastest_time


def test_given_input(my_level = "beginner"):
    if my_level == "beginner":
        time_list = [1, 2, 3, 4]
        # print(calculate_fastest_time(time_list))
    elif my_level == "pro":
        large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
        short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
        print(compute_overlap_time(large, short))
    result = 1
    expected = 4

    assert result == expected, "Fastest time is not 1" 
    #change my terminal output color to red
    

test_given_input()