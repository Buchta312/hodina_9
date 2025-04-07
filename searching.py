import os
import json

from hodina_9.generators import dna_sequence
from range import hladane_cislo

# get current working directory path
cwd_path = os.getcwd()


def read_data(sequential, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """

    file_path = os.path.join(cwd_path, sequential)
    with open(file_path, "r") as file_ob:
        data = json.load(file_ob)
        if field in data.keys():
            return data[field]
        else:
            print(f"field {field} not existing")
            return None

def linear_search(list_of_numbers, number):
    list_of_idx = []

    for idx, element in enumerate(list_of_numbers):
        if element == number:
            list_of_idx.append(idx)
        else:
            pass

    return {"positions": list_of_idx, "count": len(list_of_idx)}

def pattern_search(sequence, patern):
    list_of_dna = set()
    pattern_lengt = len(patern)

    for idx in range(0, len(sequence - pattern_lengt)):
        pattern_similarity = 0
        for idx_pattern, patern_element in enumerate(patern):
            if sequence[idx + idx_pattern] == patern_element:
                pattern_similarity = pattern_similarity + 1
            else:
                break

        if pattern_similarity == pattern_lengt:
            list_of_dna.add(idx + pattern_lengt // 2 - 1)
        else:
            pass

    return list_of_dna

def binary_search(sequence, number):
    left = 0
    right = len(sequence) - 1
    while right >= left:
        middle = (left + right) // 2
        print(sequence[middle])
        if sequence[middle] == number:
            return middle
        elif sequence[middle] > number:
            right = middle - 1
        elif sequence[middle] < number:
            left = middle + 1
    return None







def main():
    json_filename = "sequential.json"
    key_of_sequence = "unordered_numbers"
    deoxi_sequence = "dna_sequence"
    searched_patern = "ATA"
    dna_data = read_data(json_filename, deoxi_sequence)
    my_data = read_data(json_filename, key_of_sequence)
    print(my_data)
    print(dna_data)
    found_dna_sequence = pattern_search(dna_data, 0)
    found_number_linear = linear_search(my_data, 0)
    print(found_number_linear)
    print(found_dna_sequence)


if __name__ == '__main__':
    my_list = [1, 2, 5, 7]
    searched_number = 5
    found_number = linear_search(my_list, searched_number)
    print(found_number)
    main()

