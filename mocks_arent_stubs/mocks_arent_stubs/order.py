from .warehouse import Warehouse
from .mail_service import MailService, Message
from typing import Optional


class Order:
    def __init__(self, product_name: str, quantity: int) -> None:
        self.mailer: Optional[MailService] = None
        self._product_name = product_name
        self._quantity = quantity
        self._is_filled = False

    @property
    def is_filled(self):
        return self._is_filled

    def fill(self, warehouse: Warehouse) -> None:
        if not warehouse.has_inventory(self._product_name, self._quantity):
            self._send_mail(":(")
            return

        warehouse.remove(self._product_name, self._quantity)
        self._is_filled = True

    def _send_mail(self, message: str):
        if self.mailer is not None:
            self.mailer.send(Message(message))
