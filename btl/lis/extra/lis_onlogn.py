def get_ceil_index(arr, T, l, r, key):
    while r - l > 1:

        m = l + (r - l) // 2
        if arr[T[m]] >= key:
            r = m
        else:
            l = m

    return r


def lis(arr, n):
    tail_indices = [0 for i in range(n + 1)]

    prev_indices = [-1 for i in range(n + 1)]

    len = 1
    for i in range(1, n):

        if arr[i] < arr[tail_indices[0]]:

            tail_indices[0] = i

        elif arr[i] > arr[tail_indices[len - 1]]:

            prev_indices[i] = tail_indices[len - 1]
            tail_indices[len] = i
            len += 1

        else:

            pos = get_ceil_index(arr, tail_indices, -1,
                                 len - 1, arr[i])

            prev_indices[i] = tail_indices[pos - 1]
            tail_indices[pos] = i

    print("LIS of given input")
    i = tail_indices[len - 1]
    while i >= 0:
        print(arr[i], " ", end="")
        i = prev_indices[i]
    print()

    return len


if __name__ == '__main__':
    arr = [2, 5, 3, 7, 11, 8, 10, 13, 6]
    n = len(arr)

    print("LIS size\n", lis(arr, n))
