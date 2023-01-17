import json


class ReadChoicesFromFile(object):
    DEFAULT = {'mode': 'r', 'encoding': 'utf-8'}

    def __init__(self, filepath, **kwargs):
        self.filepath = filepath
        self.kwargs = kwargs or self.DEFAULT

    def read(self):
        with open(self.filepath, **self.kwargs) as file:
            choices = self.read_data_from_file(file)

        return choices

    def read_data_from_file(self, file):
        raise NotImplementedError


class JsonChoicesReader(ReadChoicesFromFile):
    def read_data_from_file(self, file):
        return json.load(file)
