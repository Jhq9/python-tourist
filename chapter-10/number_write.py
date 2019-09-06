# json模块 json.dump()存储 json.load()加载

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = "numbers.json"

with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)