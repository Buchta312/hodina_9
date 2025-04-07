import os
import json

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
    return list_of_numbers

def main():
    json_filename = "sequential.json"
    my_data = read_data(json_filename, "unordered_numbers")
    print(my_data)


if __name__ == '__main__':
    my_list = [1, 2, 5, 7]
    searched_number = 5
    found_number = linear_search(my_list, searched_number)
    main()

