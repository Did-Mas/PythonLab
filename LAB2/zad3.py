from zad2 import merge_sort_parallel, merge_sort
from matplotlib import pyplot as plt
from matplotlib import cm
import random
import time
import numpy as np

if __name__ == '__main__':

    nmb_of_processes = 6

    l = np.linspace(10, 100000, 10)

    t_s = []
    t_m = []


    for i in range(len(l)):
        randomized_array = np.random.rand(int(l[i]))
        print(f"Length: {int(l[i])}")
        print("Start single...")
        start = time.time()
        merge_sort(randomized_array)
        stop = time.time()
        t_s.append(stop-start)
        print("Done!")

        print("Start multi...")
        start = time.time()
        merge_sort_parallel(randomized_array, nmb_of_processes)
        stop = time.time()
        print("Done!")
        t_m.append(stop-start)

    plt.plot(l, t_s, "b-")
    plt.plot(l, t_m, "r-")
    plt.grid()
    plt.show()
