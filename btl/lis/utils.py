import numpy as np


def gen_input(*args):
    file_name = "input.txt"
    file = open(file_name, "w")
    file.writelines(f"{len(args)} \n")
    for n in args:
        file.write(" ".join(map(str, np.random.permutation(n))) + "\n")


if __name__ == '__main__':
    gen_input(50, 100, 200, 500, 800, 1000, 1200, 1500, 1800, 2000)
