#!/usr/bin/env python3
"""Each next element of the Fibonacci series is obtained by adding the previous two. Starting at 1 and 2,
the first 10 items will be: 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Copyright (c) 2021-2022, Roman Kaban.
License:    GPL-3.0
"""

import multi_iter

__author__ = "Roman Kaban"
__version__ = "0.9"


class Fibonacci(multi_iter.MultiIter):
    """
    An iterator class that returns a Fibonacci number each time __next__ is called.
    limit-the max number of numbers from the Fibonacci series that an instance of the class can produce. 0 - disabled
    max_value is the maximum value returned by the __next__ method. 0 - disabled
    """

    def __init__(self, max_value: int = 0, limit: int = 1000):
        super().__init__()
        """Initial setup"""
        self._counter = 0
        self._a, self._b = 0, 1
        #
        self.setup(max_value, limit)

    def make_instance(self):
        """return instance of class."""
        return Fibonacci()

    def setup(self, max_value: int, limit: int):
        """Limits setup after creation instance. For fine tune only!
            Call this method now after __init__!!!"""
        self.limit = limit
        self.max_value = max_value

    @staticmethod
    def _check_value(value: int, minimum: int, maximum: int):
        """Internal method. Do not use!"""
        if minimum < value <= maximum:
            raise StopIteration

    def __next__(self) -> int:
        """Часть протокола итератора"""
        # Проверка. Счетчик в диапазоне
        self._check_value(self.limit, 0, self._counter)

        result = self._a + self._b
        # Проверка. Результат в диапазоне
        self._check_value(self.max_value, 0, result)

        self._a = result
        self._a, self._b = self._b, self._a
        self._counter += 1
        return result

    # def reset(self):
    #    self.setup(self.max_value, self.limit)

    def __str__(self):
        """Instance string representation"""
        return f"{self.__class__.__name__} class instance at {str.upper(hex(id(self)))}. limit: {self.limit}; \
max value: {self.max_value}; counter: {self._counter}"

    def __len__(self) -> int:
        return self._counter


if __name__ == "__main__":
    F = Fibonacci(max_value=4_000_000)
    # выражение-генератор
    lg = (i for i in F if i % 2 == 0 and i < 4_000_000)
    print(f"sum: {sum(lg)}")
    #
    print(F)
