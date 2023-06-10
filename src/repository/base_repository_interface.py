from abc import ABC, abstractmethod


class BaseRepositoryInterface(ABC):
    @abstractmethod
    def get_all(self):
        ...

    @abstractmethod
    def get_by_id(self, id):
        ...
