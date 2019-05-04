from abc import ABC, abstractmethod


class InvalidOperation(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperation("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperation("Stream is already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Read file from file")


class NetworkStream(Stream):
    def read(self):
        print("Read file from Network")


class MemoryStream(Stream):
    def read(self):
        print("Read file from Memory")


f = FileStream()
f.read()
print(isinstance(f, FileStream))

#s = Stream()
m = MemoryStream()
m.read()
