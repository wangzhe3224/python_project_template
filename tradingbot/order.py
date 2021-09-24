import enum


class OrderState(enum.Enum):
    open = enum.auto()
    filled = enum.auto()
    cancelled = enum.auto()


def open_order(o: OrderState) -> OrderState:
    return {
        OrderState.filled: OrderState.filled,
        OrderState.open: OrderState.open,
        OrderState.cancelled: OrderState.cancelled,
    }[o]


def fill(o: OrderState) -> OrderState:
    return {
        OrderState.filled: OrderState.filled,
        OrderState.open: OrderState.filled,
        OrderState.cancelled: OrderState.cancelled,
    }[o]


def cancel(o: OrderState) -> OrderState:
    return {
        OrderState.filled: OrderState.filled,
        OrderState.open: OrderState.cancelled,
        OrderState.cancelled: OrderState.cancelled,
    }[o]
