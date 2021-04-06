def get_ceil_index(arr, T, l, r, key):
    while r - l > 1:

        m = l + (r - l) // 2
        if arr[T[m]] >= key:
            r = m
        else:
            l = m

    return r


def lis_onlogn(arr):
    n = len(arr)
    tail_indices = [0 for i in range(n + 1)]

    prev_indices = [-1 for i in range(n + 1)]

    length = 1
    for i in range(1, n):

        if arr[i] < arr[tail_indices[0]]:

            tail_indices[0] = i

        elif arr[i] > arr[tail_indices[length - 1]]:

            prev_indices[i] = tail_indices[length - 1]
            tail_indices[length] = i
            length += 1

        else:

            pos = get_ceil_index(arr, tail_indices, -1,
                                 length - 1, arr[i])

            prev_indices[i] = tail_indices[pos - 1]
            tail_indices[pos] = i

    # print("LIS of given input")
    # i = tail_indices[length - 1]
    # while i >= 0:
    #     print(arr[i], " ", end="")
    #     i = prev_indices[i]
    # print()

    return length


def lis_dp(arr):
    n = len(arr)

    lis = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    maximum = 0

    for i in range(n):
        maximum = max(maximum, lis[i])

    cur = maximum
    result = []
    for i in range(n):
        index = n - i - 1
        if lis[index] == cur:
            result.insert(0, arr[index])
            cur -= 1
    return len(result)


if __name__ == '__main__':
    arr = [2, 5, 3, 7, 11, 8, 10, 13, 6]
    n = len(arr)

    print("LIS size\n", lis_onlogn(arr))
