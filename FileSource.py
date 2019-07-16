from typing import List

from Source import Source
import csv
import json

SUPPORTED_TYPES: List[str] = ["csv", "json"]


class FileSource(Source):
    __doc__ = "A source for local filesystem files. If a type is specified {t}, the appropriate " \
              "python library will be used. Pass all of its parameters as a dict in readerprops".format(
                t=SUPPORTED_TYPES)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        type = self.properties["type"]
        self.readerprops = self.properties["readerprops"] if self.properties["readerprops"] else {}
        if type == "csv":
            self.reader = csv.reader

        elif type == "json":
            self.reader = json.load
        else:
            def rdr(f, **kwargs):
                return f

            self.reader = rdr

    def read(self) -> "generator for line objects":
        """Reads the file specified in the path property returining a generator"""
        with open(self.properties["path"]) as f:
            for i in self.reader(f):
                yield i


def test():
    s = FileSource()
    s.properties = {"path": "Source.py", "2": 2}
    s.properties = {"path": "Data.py"}
    # print(s.properties)
    # for i in s.read():
    #     print(i)
    help(s)


if __name__ == "__main__":
    test()
