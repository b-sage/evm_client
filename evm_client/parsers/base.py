import abc

class BaseParser(abc.ABC):

    @abc.abstractmethod
    def default_format(self):
        pass


