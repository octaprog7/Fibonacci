#!/usr/bin/env python3
"""Each next element of the Fibonacci series is obtained by adding the previous two. Starting at 1 and 2,
the first 10 items will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ..."""


class Fibonacci:
    """
    An iterator class that returns a Fibonacci number each time __next__ is called.
    limit-the max number of numbers from the Fibonacci series that an instance of the class can produce. 0 - disabled
    max_value is the maximum value returned by the __next__ method. 0 - disabled
    """

    def __init__(self, max_value=0, limit=0):
        self.limit = limit
        self.max_value = max_value
        self.counter = 0
        self.a, self.b = 0, 1

    def __next__(self):
        if 0 < self.limit <= self.counter:
            raise StopIteration

        result = self.a + self.b

        if 0 < self.max_value < result:
            raise StopIteration

        self.a = result
        self.a, self.b = self.b, self.a
        self.counter += 1
        return result

    def __iter__(self):
        return self  # FibIter()

    def reset(self):
        self.__init__(self.limit)

    def __len__(self):
        return self.counter

    def __del__(self):
        pass


if __name__ == "__main__":
    F = Fibonacci()
    L = [i for i in F if i % 2 == 0 and i < 400]
    print(f"sum: {sum(L)}")
