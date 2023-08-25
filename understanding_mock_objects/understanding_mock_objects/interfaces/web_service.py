from abc import ABC, abstractmethod


class IWebService(ABC):
    @abstractmethod
    def write(self, message: str) -> None:
        pass
