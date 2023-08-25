from abc import ABC, abstractmethod


class ILogger(ABC):
    @abstractmethod
    def write(self, text: str) -> None:
        pass


class LoggerException(Exception):
    pass
