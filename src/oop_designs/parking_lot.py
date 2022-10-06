"""

Design a parking lot


Requirements
    Parking can be single-level or multilevel.
    Types of vehicles that can be parked, separate spaces for each type of vehicle.
    Entry and exit points.
    A user can park, pay the ticket and leave



ParkingLot (Singleton)
    Floors
        Spots (interface)
            -vehicle

            +park(vehicle: Vehicle)
            
    Entrances
    Exits

    TicketManager


    +get_empty_spot()


Vehicle (interface)
    -size

    Tuck
    Car
    Motorcycle


Ticket



PaymentProcessorStrategy
    CreditCardProcessor
    BitcoinProcessor






Paid parking lot
    Tickets

Levels

Spots of different sizes

Vehicles

User

Payment



Actions

    User check in a vehicle

    User can pay a ticket

    User can checkout a vehicle



"""
