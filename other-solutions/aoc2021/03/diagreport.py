from collections import defaultdict

def gamma_epsilon(report):
    on_bit_counts = defaultdict(int)
    bitset_count = 0
    bitset_length = len(report[0])
    for bitset in report:
        bitset_count += 1
        for idx, bit in enumerate(bitset):
            if bit == '1':
                on_bit_counts[idx] += 1

    majority_bit_count = bitset_count / 2

    gamma_bit_list = ''
    epsilon_bit_list = ''
    for i in range(0, bitset_length):
        if on_bit_counts[i] == majority_bit_count:
            gamma_bit_list += 't'
            epsilon_bit_list += 't'
        elif on_bit_counts[i] > majority_bit_count:
            gamma_bit_list += '1'
            epsilon_bit_list += '0'
        else:
            gamma_bit_list += '0'
            epsilon_bit_list += '1'

    return gamma_bit_list, epsilon_bit_list
