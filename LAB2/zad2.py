import math
import multiprocessing
import random
import sys
import time


def merge(*args):
    left, right = args[0] if len(args) == 1 else args
    left_length, right_length = len(left), len(right)
    left_index, right_index = 0, 0
    merged = []
    while left_index < left_length and right_index < right_length:
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    if left_index == left_length:
        merged.extend(right[right_index:])
    else:
        merged.extend(left[left_index:])
    return merged


def merge_sort(data):
    length = len(data)
    if length <= 1:
        return data
    middle = length / 2
    left = merge_sort(data[:int(middle)])
    right = merge_sort(data[int(middle):])
    return merge(left, right)


def merge_sort_parallel(data, processes):
    # processes = multiprocessing.cpu_count()
    with multiprocessing.Pool(processes=processes) as pool:
        size = int(math.ceil(float(len(data)) / processes))
        data = [data[i * size:(i + 1) * size] for i in range(processes)]
        data = pool.map(merge_sort, data)
        while len(data) > 1:
            extra = data.pop() if len(data) % 2 == 1 else None
            data = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]
            data = pool.map(merge, data) + ([extra] if extra else [])
        return data[0]


if __name__ == "__main__":
    size = int(sys.argv[-1]) if sys.argv[-1].isdigit() else 1000
    data_unsorted = [random.randint(0, size) for _ in range(size)]
    data_sorted = merge_sort_parallel(data_unsorted)
    print(data_unsorted)
    print(data_sorted)
    print(sorted(data_unsorted) == data_sorted)

