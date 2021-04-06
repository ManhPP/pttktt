import numpy as np


def gen_input(*args):
    file_name = "input.txt"
    file = open(file_name, "w")
    file.writelines(f"{len(args)} \n")
    for n in args:
        file.write(" ".join(map(str, np.random.permutation(n))) + "\n")


if __name__ == '__main__':
    gen_input(100, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 800000, 1000000, 1200000, 1500000, 2000000)
