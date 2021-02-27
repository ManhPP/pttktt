import math
from sort import radix_sort
from veb import VEB


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
    while m <= n:
        is_break = False

        num_block = math.ceil(n / m)

        sorted_s = [(int(i / m), v) for i, v in enumerate(s)]
        radix_sort(sorted_s, key=lambda x: x[1])
        sorted_block_s = {i: {} for i in range(num_block)}

        for element in sorted_s:
            sorted_block_s[element[0]][element[1]] = len(sorted_block_s[element[0]])

        B = VEB(math.ceil(2 * m))
        k = 0
        prev_list = []

        for block in range(num_block):
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
                    B.delete(B.get_successor(key=key))
            prev_list = []
            for i in range(2 * m):
                if B.has_member(i):
                    prev_list.append(r_sorted_block_s[i])
                    B.delete(i)

            if k >= 2 * m:
                is_break = True
                break

        if not is_break:
            return k

        new_m = math.ceil(math.pow(m, math.log(m)))
        if new_m <= m:
            m += 1
        else:
            m = new_m


if __name__ == '__main__':
    s = [12, 8, 9, 1, 11, 6, 7, 2, 10, 4, 5, 3]
    print(main(s))
