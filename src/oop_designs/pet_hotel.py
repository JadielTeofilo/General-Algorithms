"""

Design a Pet Hotel


Hotel
employees

People can go and leave their pets
People can take their pets

dogs cats
hotel is going to have capacity, divided on small, medium and large pets

actions 
leave a dog
get a dog back


PetHotel (singleton)
Booking
Room
    RoomQueen
    Room2

PaymentProcessor (Strategy)
    CreditCardProcessor
    MoneyProcessor


"""
import collections
import dataclasses
from typing import List



Range = collections.namedtuple('Range', 'start end')


@dataclasses.dataclass
class Capacity:
    uid: str
    name: str
    size: Range


@dataclasses.dataclass
class Pet:
    name: str
    size: int
    owner: Person


@dataclasses.dataclass
class Room:
    capacity: Capacity
    pet: Optional[Pet]
    uid: str = uuid.uuid4().hex



class PetHotel:

    def __init__(self) -> None:
        self._capacities: SortedList[Capacity] = self._build_capacities()  # TODO
        self._capacity_slots: Dict[str, int] = self._build_capacity_slots()  #TODO
        self._rooms: Dict[str, Room] = dict() # Maps room id to a room
        self._pets: Dict[str, Room] = dict()  # Maps from pet id to a room

    def leave_a_pet(self, pet: Pet) -> str:  # TODO
        capacity: Optional[Capacity] = self._find_valid_capacity(pet)  # TODO
        if not capacity:
            raise NoCapacityError()  # TODO
        self.capacity_slots[capacity.uid] -= 1
        room: Room = Room(capacity, pet)
        self.rooms[room.uid] = room
        return room.uid

    def get_pet_back(self, room_id: str = None, pet_id: str = None) -> Pet:
        root: Optional[Room] = None
        if room_id and room_id in self.rooms:
            room: Room = self.rooms[room_id]
        if pet_id and pet_id in self.pets:
            room: Room = self.pets[pet_id]
        if not room:
            raise ValueError('Missing valid input')
        self.capacity_slots[room.capacity.uid] += 1
        return self.rooms.pop(room_id).pet
        
        



