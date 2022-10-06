"""

Stock Data: Imagine you are building some sort of service that will be called by up to 1,000 client
applications to get simple end-of-day stock price information (open, close, high, low). You may
assume that you already have the data, and you can store it in any format you wish. How would
you design the client-facing service that provides the information to client applications? You are
responsible for the development, rollout, and ongoing monitoring and ma intenance of the feed.
Describe the different methods you considered and why you would recommend your approach.
Your service can use any technologies you wish, and can distribute the information to the client
applications in any mechanism you choose.




requirements

be able to get_stock_info of a given stock on a given day, or a list of those


non functional

1000 clients
    assume each client does an average of 10000 requests
    10 million requests a day 
    ~500 thousand requests per hour
    ~10 thousand requests per minute
    ~200 requets per second

read heavy system


           Client 

             |        


            API

             |


             DB



closing_price
    id: int
    date: date
    open: int  # in cents
    close: int  # in cents
    high: int 
    low: int
    stock_id: int


We can`t give direct access to the clients to the dbs cuz of security reasons





"""
