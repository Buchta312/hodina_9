import os
import json

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

def main():
    pass


if __name__ == '__main__':
    main()
    json_filename = "sequential.json"
    my_data = read_data(json_filename, "unordered_numbers")