import os
from collections import namedtuple
from typing import Type
import json

Sentence = namedtuple('Sentence', ['sentence', 'file'])
File = namedtuple('File', ['name', 'path', 'offset']) #the inside
#File = namedtuple('File', 'name path offset') #the inside

def initialize(path : str) -> None:
    path = rf'{path}'
    root_name = os.path.basename(path)
    details = {}
    for root, dirs, files in os.walk(path, topdown=True):
        for _file in files:
            fullpath = os.path.join(root,_file)
            with open(fullpath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                sentences = dict(zip(lines, range(len(lines)))) #option 2 - delete duplicated sentences - takes he last one in the file
               # details = {Sentence(keys, File(_file, fullpath, values)) for keys,values in sentences.items()}
                for keys, values in sentences.items():
                    if keys in details.keys():
                        details[keys].append(File(_file, fullpath, values))
                    else:
                        details[keys] = [File(_file, fullpath, values)]
               #     print(details)

    with open('data4.txt', 'w') as data_file:
       data_file.write(json.dumps(details))



if __name__ == '__main__':
    initialize("C:/cygwin64/compiler/2021-archive")





