"""

Design a Vending Machine


Add items to the vending machine in fixed number of slots
Payment using card or cash
Select item to dispense


assume a corner vending machine
It has drinks
    each drink has a differnt brand, diff price, diff name
It has snacks
    name, price, brand

A machine has slots
    each slot can hold multiple values

Payment can be done in two forms


You can buy an item

"""
from typing import Optional
import dataclasses


@dataclasses.dataclass
class Product:
    name: str

    @property
    def price():
        raise NotImplemented


@dataclasses.dataclass
class Slot:
    id: int
    product: Optional[Product] # TODO
    amount: int


class VendingMachine:

    def __init__(self) -> None:
        slots: List[Slot] = []
        slot_by_id: Dict[id, Slot] = dict()

    def buy(self, slot_id: int, money: int) -> int: 
        



