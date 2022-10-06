"""
 Othello: Othello is played as follows: Each Othello piece is white on one side and black on the other.
When a piece is surrounded by its opponents on both the left and right sides, or both the top and
bottom, it is said to be captured and its color is flipped. On your turn, you must capture at least one
of your opponent's pieces. The game ends when either user has no more valid moves. The win is
assigned to the person with the most pieces. Implement the object-oriented design for Othello.


Is it electronic or the representation of the phisical game
    electronic


Should we worry about another interface other than the game being played (user register, matchmaking and such)

How long does a user have to make a play, what happens if it does nothing


MatchHandler
    matches: List[Match]

    


Match
    grid: List[List[Optional[Piece]]]
    pieces: List[Pieces]


    is_over()
    get_winner()
    move()
    capture()

Player
    
    make_move()
    


Piece
    side_up: Color
    owner: Player




"""
