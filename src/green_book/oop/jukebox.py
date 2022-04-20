"""
Jukebox: Design a musical jukebox using object-oriented principles.

Who is going to use this jukebox? 
Where is it going to get its songs from?
Will it have a paying system associated with it?
How do we want to use it?


1 - Remove ambiguity
2 - Define entities
    JukeBox
    Artist
    Song
    Album
    Playlist
    PlayQueue

3 - Define relations
JukeBox has all the others
artist has many songs
album has many songs
playlist has many songs
playqueue has many songs lined up

4 - Define actions

JukeBox 
    add a song/album/playlist to play
    ...


------
TakeAways

Think about creating the class for the thing it self (JukeBox)
    It will have the attributes for all the other meaningfull objects and one or another useful general method



"""
