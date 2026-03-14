# Hide complex implementation

from abc import ABC, abstractmethod
class Car(ABC):

    @abstractmethod
    def start_engine(self):
        pass


class Toyota(Car):
    def start_engine(self):
        print("Toyota engine started")


class Tesla(Car):
    def start_engine(self):
        print("Tesla electric motor started")

car1 = Toyota()
car2 = Tesla()

car1.start_engine()
car2.start_engine()