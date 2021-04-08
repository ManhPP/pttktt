
def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[n-1] == Y[m-1]:
        return 1 + lcs(X, Y, m-1, n-1)
    else:
        return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))

line = input().split()
n = int(line[0])
m = int(line[1])

X = input().split()
Y = input().split()

print(lcs(X, Y, m, n))

