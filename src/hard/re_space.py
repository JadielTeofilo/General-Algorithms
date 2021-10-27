"""
Re-Space: Oh, no! You have accidentally removed all spaces, punctuation, and capitalization in a
lengthy document. A sentence like "I reset the computer. It still didn`t boot!"
became"iresetthecomputeritstilldidntboot': You'll deal with the punctuation and capi-
talization later; right now you need to re-insert the spaces. Most of the words are in a 
dictionary but a few are not. Given a dictionary (a list of strings) and the 
document (a string), design an algorithm to unconcatenate the 
document in a way that minimizes the number of unrecognized characters.


A trie does the trick 

fill a trie with the dictionary

find the start and end indexes of the words



"""
