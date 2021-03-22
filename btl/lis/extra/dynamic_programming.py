def lis(arr):
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
    return result


if __name__ == '__main__':
    arr = [12, 8, 9, 1, 11, 6, 7, 2, 10, 4, 5, 3, 15, 13, 14]
    print("lis is {}".format(lis(arr)))
