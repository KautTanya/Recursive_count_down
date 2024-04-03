"""recursive_count_down"""
import time


def recursive_count_down(n):
    """recursive_count_down"""
    if n == 1:
        return 1
    else:
        print(n)
        time.sleep(1)
        return recursive_count_down(n - 1)


print(recursive_count_down(10))
