"""
MCON 264 - Module 2 - Demo 1
Two correct answers. One unusable solution.

This is the Contains Duplicate problem from Quiz 1, solved two ways.
Both return the right answer every time. Run this and watch what happens
to each one as the list gets bigger.

    python3 demo1_growth.py
"""
import random
import time


def has_duplicate_brute(nums):
    """Compare every element against every element after it."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


def has_duplicate_sorted(nums):
    """Sort a copy, then check neighbours."""
    ordered = sorted(nums)          # a copy - we do not touch the caller's list
    for i in range(len(ordered) - 1):
        if ordered[i] == ordered[i + 1]:
            return True
    return False


def timed(fn, nums):
    start = time.perf_counter()
    fn(nums)
    return time.perf_counter() - start


def main():
    print()
    print("  Worst case: no duplicates, so both must look at everything.")
    print()
    print(f"  {'n':>7}  {'brute force':>13} {'x':>6}   {'sorted scan':>13} {'x':>6}")
    print("  " + "-" * 56)

    prev_brute = prev_sort = None
    for n in (500, 1000, 2000, 4000):
        nums = random.sample(range(n * 10), n)   # guaranteed no duplicates

        t_brute = timed(has_duplicate_brute, nums)
        t_sort = timed(has_duplicate_sorted, nums)

        r_brute = f"{t_brute / prev_brute:.1f}x" if prev_brute else "-"
        r_sort = f"{t_sort / prev_sort:.1f}x" if prev_sort else "-"

        print(f"  {n:>7}  {t_brute * 1000:>10.2f} ms {r_brute:>6}   "
              f"{t_sort * 1000:>10.2f} ms {r_sort:>6}")

        prev_brute, prev_sort = t_brute, t_sort

    print()
    print("  The x column is the question. Every row DOUBLES n.")
    print("  What did each solution do in response?")
    print()


if __name__ == "__main__":
    main()
