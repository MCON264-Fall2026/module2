"""
MCON 264 - Module 2 - Demo 2
What does a list operation actually cost?

A Python list is one contiguous block of slots with some slack at the end.
That single fact explains every number this program prints.

Run it all, or run one part at a time by changing WHICH below.

    python3 demo2_list_costs.py
"""
import timeit

WHICH = "all"          # "all", "1", "2", or "3"
SIZES = (1000, 2000, 4000, 8000)


def bench(stmt, setup, number):
    """Average microseconds for one execution of stmt."""
    total = timeit.timeit(stmt, setup=setup, number=number)
    return total / number * 1e6


def table(title, question, cols, setup, reps):
    """cols: list of (label, stmt). reps: int, or a function of n."""
    print()
    print(f"  {title}")
    print(f"  {question}")
    print()
    header = "".join(f"{label:>18}" for label, _ in cols)
    print(f"  {'n':>7}{header}")
    print("  " + "-" * (7 + 18 * len(cols)))
    for n in SIZES:
        number = reps(n) if callable(reps) else reps
        cells = ""
        for _, stmt in cols:
            us = bench(stmt, setup.format(n=n), number)
            cells += f"{us:>14.3f} us"
        print(f"  {n:>7}{cells}")
    print()


def part1():
    table(
        "PART 1 - adding an item",
        "Predict first: which one slows down as the list grows?",
        [("append(x)", "data.append(99)"), ("insert(0, x)", "data.insert(0, 99)")],
        setup="data = list(range({n}))",
        reps=4000,
    )


def part2():
    table(
        "PART 2 - removing an item",
        "Same question. One of these is the deal() from your Lab 1 Deck.",
        [("pop()", "data.pop()"), ("pop(0)", "data.pop(0)")],
        setup="data = list(range({n}))",
        reps=lambda n: n // 2,          # never drain the list
    )


def part3():
    table(
        "PART 3 - finding an item",
        "Looking for a value that is NOT there, so it has to check everywhere.",
        [("x in list", "-1 in data"), ("data[0]", "data[0]")],
        setup="data = list(range({n}))",
        reps=2000,
    )


if __name__ == "__main__":
    if WHICH in ("all", "1"):
        part1()
    if WHICH in ("all", "2"):
        part2()
    if WHICH in ("all", "3"):
        part3()
    print("  One rule about how a list is laid out in memory explains all three tables.")
    print("  What is it?")
    print()
