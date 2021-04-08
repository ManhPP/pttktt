line = input().split()
n = int(line[0])
val = int(line[1])

arr = input().split()
for i, v in enumerate(arr):
    arr[i] = int(v)

count = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if arr[i] + arr[j] + arr[k] == val:
                count += 1

print(count)