def counting_sort(arr, exp, key):
    n = len(arr)

    output = [0] * n
    count = [0] * 10

    for i in range(0, n):
        index = (key(arr[i]) / exp)
        count[int(index % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (key(arr[i]) / exp)
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1

    for i in range(0, len(arr)):
        arr[i] = output[i]


def radix_sort(arr, key=lambda x: x):
    max_element = key(max(arr, key=key))

    exp = 1
    while max_element / exp > 0:
        counting_sort(arr, exp, key=key)
        exp *= 10


if __name__ == '__main__':

    arr = [250, 38, 88, 95, 802, 29, 1, 70]
    radix_sort(arr)

    for i in range(len(arr)):
        print(arr[i])
