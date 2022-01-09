#!/usr/bin/env python3
from fib import Fibonacci


if __name__ == '__main__':
    F = Fibonacci(max_value=4_000_000)
    # выражение-генератор
    lg = (i for i in F if i % 2 == 0 and i < 4_000_000)
    print(f"sum: {sum(lg)}")