line = input().split()
n = int(line[0])
m = int(line[1])

mat = [[-1 for i in range(n)] for j in range(n)]

for _ in range(m):
    line = input().split()
    i = int(line[0])
    j = int(line[1])
    c = int(line[2])
    mat[i-1][j-1] = c

result = []
cur = 0
cost = 0

for _ in range(n-1):
    min_c = 1e6
    result.append(cur)
    for i in range(n):
        if mat[cur][i] != -1 and mat[cur][i] < min_c and i not in result:
            min_c = mat[cur][i]
            next_point = i

    cur = next_point
    cost+= min_c

cost += mat[cur][0]
print(cost)