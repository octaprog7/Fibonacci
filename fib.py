#!/usr/bin/env python3
"""Each next element of the Fibonacci series is obtained by adding the previous two. Starting at 1 and 2,
the first 10 items will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Copyright (c) 2021-2022, Roman Kaban.
License:    GPL-3.0
"""

__author__ = "Roman Kaban"
__version__ = "0.9"


class Fibonacci:
    """
    An iterator class that returns a Fibonacci number each time __next__ is called.
    limit-the max number of numbers from the Fibonacci series that an instance of the class can produce. 0 - disabled
    max_value is the maximum value returned by the __next__ method. 0 - disabled
    """

    def __init__(self, max_value=0, limit=0):
        self._init_()
        self._set_limits(max_value, limit)

    def _set_limits(self, max_value=0, limit=0):
        """Limits setup"""
        self.limit = limit
        self.max_value = max_value

    def _init_(self):
        """Ititial setup"""
        self._counter = 0
        self._a, self._b = 0, 1

    def __next__(self):
        if 0 < self.limit <= self._counter:
            raise StopIteration

        result = self._a + self._b

        if 0 < self.max_value < result:
            raise StopIteration

        self._a = result
        self._a, self._b = self._b, self._a
        self._counter += 1
        return result

    def __iter__(self):
        return self  # FibIter()

    def reset(self, max_value=0, limit=0):
        self._init_()
        self._set_limits(max_value, limit)

    def __len__(self):
        return self._counter

    def __del__(self):
        pass


if __name__ == "__main__":
    F = Fibonacci()
    L = [i for i in F if i % 2 == 0 and i < 400]
    print(f"sum: {sum(L)}")
