"""
created a jsonFileHandle module that you can import in other Python files to access the readJsonFile function.
"""
import json

def readJsonFile(fileName):
    data = ""
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data


