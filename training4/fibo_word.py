def fib_word(n):
    Sn_1 = "0"
    Sn = "01"
    tmp = ""
    for i in range(2, n + 1):
        tmp = Sn
        Sn += Sn_1
        Sn_1 = tmp
    return Sn

n = int(input())

s = fib_word(n)
