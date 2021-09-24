import pytest

from tradingbot.order import OrderState, open_order


def test_open():
    assert open_order(OrderState.filled) is OrderState.filled
