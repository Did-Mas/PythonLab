from random import randint

N = 100

random_list = []

for i in range(N):
    random_list.append(randint(0, 50))

print("Input:", random_list)

print("____________________________")

sorted_check = sorted(random_list)
print("Sorted with built-in function:", sorted_check)

def swap(lst, a, b):
    temp = lst[a]
    lst[a] = lst[b]
    lst[b] = temp
    return lst


def bubble_sort(to_sort):
    for j in range(len(to_sort)-1, 0, -1):
        p = 1
        for i in range(j):
            if to_sort[i] > to_sort[i+1]:
                to_sort = swap(to_sort, i, i+1)
                p = 0
        if p:
            break
    return to_sort

def insert_sort(to_sort):
    n = len(to_sort)
    for j in range(n-2, -1, -1):
        x = to_sort[j]
        i = j + 1
        while (i < n) and (x > to_sort[i]):
            to_sort[i-1] = to_sort[i]
            i += 1
        to_sort[i-1] = x
    return to_sort

sorted_bubble = bubble_sort(random_list)
print("____________________________")
print("Sorted with own bubble sort:", sorted_bubble)
print("Same result?: ", sorted_check == sorted_bubble)

sorted_insert = insert_sort(random_list)
print("____________________________")
print("Sorted with own insert sort:", sorted_insert)
print("Same result?: ", sorted_check == sorted_insert)