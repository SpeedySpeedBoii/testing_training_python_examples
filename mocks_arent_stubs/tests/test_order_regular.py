import pytest
from mocks_arent_stubs.warehouse import Warehouse
from mocks_arent_stubs.order import Order
from mocks_arent_stubs.mail_service import MailService, Message


TALISKER = "Talisker"
HIGHLAND_PARK = "Highland Park"


@pytest.fixture
def warehouse():
    warehouse = Warehouse()
    warehouse.add(TALISKER, 50)
    warehouse.add(HIGHLAND_PARK, 25)
    return warehouse


def test_order_is_filled_if_enough_in_warehouse(warehouse):
    order = Order(TALISKER, 50)
    order.fill(warehouse)
    assert order.is_filled
    assert warehouse.get_inventory(TALISKER) == 0


def test_order_does_not_remove_if_not_enough(warehouse):
    order = Order(TALISKER, 51)
    order.fill(warehouse)
    assert not order.is_filled
    assert warehouse.get_inventory(TALISKER) == 50


# Should've been called MailServiceSpy
class MailServiceStub(MailService):
    def __init__(self):
        self._messages: list[Message] = []

    def send(self, msg: Message) -> None:
        self._messages.append(msg)

    def number_sent(self) -> int:
        return len(self._messages)


def test_order_sends_mail_if_unfilled(warehouse):
    order = Order(TALISKER, 51)
    mailer = MailServiceStub()
    order.mailer = mailer
    order.fill(warehouse)
    assert mailer.number_sent() == 1
