array = [1, 2, 3, 4, 5, 6, 7]


def Rotate_arr(arr, n):
    n %= len(arr)
    fst_arr = arr[:n]
    sec_arr = arr[n:]
    return sec_arr + fst_arr


array = Rotate_arr(array, 2)
print(array)
