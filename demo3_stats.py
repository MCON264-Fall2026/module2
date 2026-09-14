"""
MCON 264 - Module 2 - Demo 3
demo3_stats.py - the code under test. This is the file we fix live.
"""


def average(nums):
    """Return the average of a list of numbers."""
    return sum(nums) / len(nums)


def largest(nums):
    """Return the largest number in the list."""
    biggest = nums[0]
    for n in nums:
        if n > biggest:
            biggest = n
    return biggest
