import math

from sort import radix_sort
from veb import VEB
import timeit


def merge(block_s, prev_list):
    result = {}
    i = j = k = 0
    n_block_s = len(block_s)
    n_prev_list = len(prev_list)
    key_list_of_block = list(block_s.keys())

    while i < n_block_s and j < n_prev_list:
        if key_list_of_block[i] < prev_list[j]:
            result[key_list_of_block[i]] = k
            i += 1
        else:
            result[prev_list[j]] = k
            j += 1
        k += 1

    while i < n_block_s:
        result[key_list_of_block[i]] = k
        i += 1
        k += 1
    while j < n_prev_list:
        result[prev_list[j]] = k
        j += 1
        k += 1

    return result


def main(s):
    n = len(s)
    m = 1

    sorted_s = [(i, v) for i, v in enumerate(s)]
    radix_sort(sorted_s, key=lambda x: x[1])

    while m <= n:
        track_dict = {}
        is_break = False

        num_block = math.ceil(n / m)

        sorted_block_s = {i: {} for i in range(num_block)}

        for element in sorted_s:
            block = int(element[0]/m)
            sorted_block_s[block][element[1]] = len(sorted_block_s[block])

        B = VEB(2 * m)
        k = 0
        r_sorted_block_s = {}
        block = 0
        for block in range(num_block):
            prev_list = []
            for i in range(2 * m):
                if B.has_member(i):
                    prev_list.append(r_sorted_block_s[i])
                    B.delete(i)

            sorted_block_s[block] = merge(sorted_block_s[block], prev_list)
            r_sorted_block_s = {i: j for j, i in sorted_block_s[block].items()}

            if len(r_sorted_block_s) >= 2 * m:
                is_break = True
                break

            for i in prev_list:
                B.insert(sorted_block_s[block][i])

            start_ind = block * m
            # end_ind = start_ind + m
            if block < num_block - 1:
                end_ind = start_ind + m
            else:
                end_ind = start_ind + (n % m if n % m else m)

            for i in range(start_ind, end_ind):
                key = sorted_block_s[block][s[i]]
                B.insert(key=key)
                if key == B.max:
                    k += 1
                else:
                    suc_of_key = B.get_successor(key=key)
                    suc_of_suc_of_key = B.get_successor(key=suc_of_key)
                    pred_of_key = B.get_predecessor(key=key)
                    if suc_of_key is not None:
                        if suc_of_suc_of_key is not None and r_sorted_block_s[suc_of_suc_of_key] not in track_dict.keys():
                            track_dict[r_sorted_block_s[suc_of_suc_of_key]] = r_sorted_block_s[suc_of_key]
                        if pred_of_key is not None and r_sorted_block_s[suc_of_key] not in track_dict.keys():
                            track_dict[r_sorted_block_s[suc_of_key]] = r_sorted_block_s[pred_of_key]
                    B.delete(suc_of_key)

            if k >= 2 * m:
                is_break = True
                break

        if not is_break:
            result = [r_sorted_block_s[B.max]]
            for _ in range(k-1):
                if result[0] in track_dict.keys():
                    result.insert(0, track_dict[result[0]])
                else:
                    result.insert(0, r_sorted_block_s[B.get_predecessor(sorted_block_s[block][result[0]])])
            return k, result

        new_m = math.ceil(math.pow(m, math.log(m)))
        if new_m <= m:
            m += 1
        elif new_m > n:
            m = n
        else:
            m = new_m


def core_alg(s):
    n = len(s)

    B = VEB(n)
    k = 0
    for key in s:
        B.insert(key=key)
        if key == B.max:
            k += 1
        else:
            B.delete(B.get_successor(key=key))
    return k


if __name__ == '__main__':
    # s = [12, 8, 9, 1, 11, 6, 7, 2, 10, 4, 5, 3, 15, 13, 14]
    # print(main(s))

    with open("input.txt", "r") as file:
        with open("result.txt", "w") as output_file:
            line = file.readline()
            num_test = int(line)
            for test in range(num_test):
                s = [int(i) for i in file.readline().split()]

                start = timeit.default_timer()
                k = main(s)
                time = timeit.default_timer() - start
                output_file.write(f"{k}-{len(s)}-{time} \n")

    # with open("input.txt", "r") as file:
    #         with open("result.txt", "a") as output_file:
    #             line = file.readline()
    #             num_test = int(line)
    #             for test in range(num_test):
    #                 s = [int(i) for i in file.readline().split()]
    #
    #                 start = timeit.default_timer()
    #                 k = core_alg(s)
    #                 time = timeit.default_timer() - start
    #                 output_file.write(f"{k}-{len(s)}-{time} \n")
