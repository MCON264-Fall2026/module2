"""
MCON 264 - Module 2 - Demo 3
demo3_teststats.py - the tests for demo3_stats.py

Rules pytest follows, and they are not negotiable:
  - each test function must start with  test_
  - a test passes if nothing raises. That is what assert is for.
  - pytest DISCOVERS files named  test_*.py  or  *_test.py

Note on this file's name. "demo3_teststats.py" matches neither discovery
pattern, so a bare "python3 -m pytest" will report "no tests ran". Name the
file on the command line and it runs fine:

    python3 -m pytest demo3_teststats.py -v

That is rule 1 from the lecture.
"""
from demo3_stats import average, largest


def test_average_of_three_numbers():
    assert average([1, 2, 3]) == 2


def test_average_of_one_number():
    assert average([7]) == 7


def test_average_of_empty_list_is_zero():
    # An empty class has no average grade. It should not crash.
    assert average([]) == 0


def test_largest_finds_the_max():
    assert largest([3, 9, 4]) == 9


def test_largest_when_all_negative():
    assert largest([-5, -2, -9]) == -2
