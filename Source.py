from Data import Data
from abc import ABC, abstractmethod
from collections import defaultdict

class Source(Data, ABC):

    def __init__(self, **kwargs):
        self.__properties = defaultdict(None)
        self.__properties.update(kwargs)

    @abstractmethod
    def read(self) :
        pass

    @property
    def properties(self):
        return self.__properties
    
    @properties.setter
    def properties(self, value):
        if self.__properties:
            self.__properties.update(value)
        else:
            self.__properties = value



if __name__=="__main__":
    pass