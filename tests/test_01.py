from aoc import day_01
from aoc.load_data import get_test_data


test_data = get_test_data(1)
expected_result_a = 7

def test_day_1_a():
    assert day_01.part_1(test_data) == expected_result_a