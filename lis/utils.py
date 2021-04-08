import numpy as np
import pandas as pd


def gen_input(*args):
    file_name = "input.txt"
    file = open(file_name, "w")
    file.writelines(f"{len(args)} \n")
    for n in args:
        file.write(" ".join(map(str, np.random.permutation(n))) + "\n")


def read(*args):
    result = {}
    for file in args:
        with open(file) as f:
            for line in f.readlines():
                line = line.split('-')
                if line[1] not in result.keys():
                    result[line[1]] = {"k": line[0], file: float(line[2])}
                else:
                    result[line[1]][file] = float(line[2])
    df = pd.DataFrame(result).transpose()
    df.to_excel("result2.xlsx")


if __name__ == '__main__':
    # gen_input(100, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 800000, 1000000, 1200000, 1500000,
    #           2000000)

    read("result_main.txt", "result_core.txt", "result_onlogn.txt")
