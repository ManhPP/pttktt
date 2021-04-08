n = int(input())

arr = input().split()
for i, v in enumerate(arr):
    arr[i] = int(v)

M = [[None]*n for _ in range(n)]

for i in range(n):
    M[i][i] = i;

for i in range(n):
    for j in range(i+1,n):
        if M[i][j - 1] is not None and arr[M[i][j - 1]] < arr[j]:
            M[i][j] = M[i][j - 1];
        else:
            M[i][j] = j;

m = int(input())
s = 0
for _ in range(m):
    line = input().split()
    i = int(line[0])
    j = int(line[1])
    s += arr[M[i][j]]

print(s)