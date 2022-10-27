#!/usr/bin/python3
"""Define a class FileStorage"""

import os
import json

class FileStorage:
    """Serializes and deserializes instance from and to JSON  file """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k,v in self.__objects.items()}, f)

    def reload(self):
        if not os.path.exists(self.__file_path):
            return

        with open(self.__file_path, 'r') as f:
            dsd = None

            try:
                dsd = json.load(f)
            except json.JSONDecodeError:
                pass

            if dsd is None:
                return

