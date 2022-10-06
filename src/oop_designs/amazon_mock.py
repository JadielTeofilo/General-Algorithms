"""

Design a Transportation System for a City:


Multiple transportation mediums
People
Time
Locations

Customer is the passenger 
	The customer can traverse the city, going from a location to another
  The customer can have Tickets 
  	Tickets will change according to the method of transport
  	A ticket gets you to your destination, no matter how far
  The customer can use different transportation methods: Buses, Metro


TransportationSystem

Passenger
Tickets (abstract)

TransportationMethod (abstract)

Locations


if you go to get on a bus, you provide a bus ticket, 

CityA ------------------------------ CityB
1) person boards the bus in cityA

2) move the bus to cityB



Amazon Photos:

Design an API for uploading/displaying user photos...



follow up: small can park in medium/large, medium can park in large

final int SMALL = 0;
final int MEDIUM = 1;
final int LARGE = 2;

"""

import abc
import enum
import dataclass
import uuid


DEFAULT_CAPACITY = 10
BUS_CAPACITY = 40


class TicketType(enum.Enum):
  bus_ticket = 1
  metro_ticket = 2
  

@dataclasses.dataclass
class TransportationMethod(abc.ABC):
  _current_location_index: int
  _intinerary: List[Location]
  _passengers: List[Passenger]
  
  @property
  def _capacity(self) -> int:
    return DEFAULT_CAPACITY

  @abc.abstractmethod
  def board(self, ticket: Ticket, passenger: Passenger) -> bool:
    pass
  
  @abc.abstractmethod
  def leave(self, passenger: Passenger) -> bool:
    pass
  
  def move(self) -> None:
    self._current_location_index = (self._current_location_index + 1) % len(self._intinerary)
    for passenger in self._passengers:
      passenger.move(self._intinerary[self._current_location_index])  # TODO


@dataclasses.dataclass
class Bus(TransportationMethod):
  _capacity: int = BUS_CAPACITY
  
  def board(self, ticket: Ticket, passenger: Passenger) -> bool:
    if not ticket:
      raise ValueError('Must Have a ticket')
    if not self.passenger.has_ticket(ticket):  # TODO
      raise ValueError('Passenger does not own the ticket')
    if len(self._passengers) >= self._capacity:
    	return False
    
    passenger.consume_ticket(ticket)  # TODO
    self._passengers.append(passenger)
    return True   
    

@dataclasses.dataclass
class Ticket(abc.ABC):
  _uid: str = uuid.uuid4().hex
	# TODO diff tickets for disabled people
  
  @abc.abstractmethod
  def get_type(self) -> TicketType:
    pass

  
class BusTicket(Ticket):
  def get_type(self) -> TicketType:
    return TicketType.bus_ticket  

  
class MetroTicket(Ticket):
  def get_type(self) -> TicketType:
    return TicketType.metro_ticket  


@dataclasses.dataclass
class Passenger:
	_location: Location
  _name: str
  _tickets: List[Ticket]
	_uid: str = uuid.uuid4().hex
  


    
"""
1) Passenger + Ticket
"""




