from entities.Board import Board
from entities.Player import Player
from src.game import Game


b = Board()
p1 = Player("P1")
p2 = Player("P2")
p3 = Player("P3")
p4 = Player("P4")
g = Game(board=b, players=[p1,p2,p3,p4])
g.start()


