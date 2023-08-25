from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Message:
    data: str


class MailService(ABC):
    @abstractmethod
    def send(self, msg: Message) -> None:
        pass
