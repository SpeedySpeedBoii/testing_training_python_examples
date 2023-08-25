import pytest
from mocks_arent_stubs.warehouse import Warehouse
from mocks_arent_stubs.mail_service import MailService
from mocks_arent_stubs.order import Order
from mock import Mock, call


TALISKER = "Talisker"


def test_filling_removes_inventory_if_in_stock():
    order = Order(TALISKER, 50)
    warehouse = Mock(spec=Warehouse)
    warehouse.has_inventory.return_value = True

    order.fill(warehouse)

    warehouse.assert_has_calls(
        [
            call.has_inventory(TALISKER, 50),
            call.remove(TALISKER, 50)
        ],
        any_order=False
    )
    assert order.is_filled


def test_filling_does_not_remove_if_not_enough_in_stock():
    order = Order(TALISKER, 51)
    warehouse = Mock(spec=Warehouse)
    warehouse.has_inventory.return_value = False

    order.fill(warehouse)

    assert not order.is_filled


def test_order_sends_mail_if_unfilled():
    order = Order(TALISKER, 51)
    warehouse = Mock(spec=Warehouse)
    mailer = Mock(spec=MailService)
    order.mailer = mailer
    warehouse.has_inventory.return_value = False

    order.fill(warehouse)

    mailer.send.assert_called_once()
