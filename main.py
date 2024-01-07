from entities.board import Board
from entities.player import Player
from src.game import Game
from entities.fields import *


b = Board([DummyField("start"), ColorProperty("Mediterranean Avenue", "brown", 60, 30, 15, [2, 10, 30, 90, 160, 250]), ChooseField("Community Chest"), ColorProperty("Baltic Avenue", "brown", 60, 30, 15, [4, 20, 60, 180, 320, 450]), PayField("Income Tax", 200), Railroad("Reading Railroad", 200, 100, [25, 50, 100, 200]), ColorProperty("Oriental Avenue", "lightblue", 100, 50, 50, [6, 30, 90, 270, 400, 550]), ChooseField("Chance"), ColorProperty("Vermont Avenue", "lightblue", 100, 50, 50, [6, 30, 90, 270, 400, 550]), ColorProperty("Connecticut Avenue", "lightblue", 120, 60, 50, [8, 40, 100, 300, 450, 600]), DummyField("Jail"), ColorProperty("St. Charles Place", "pink", 140, 70, 100, [10, 50, 150, 450, 625, 750]), Utility("Electric Company", 150, 75, [4, 10]), ColorProperty("States Avenue", "pink", 140, 70, 100, [10, 50, 150, 450, 625, 750]), ColorProperty("Virginia Avenue", "pink", 160, 80, 100, [12, 60, 180, 500, 700, 900]), Railroad("Pennsylvania Railroad", 200, 100, [25, 50, 100, 200]), ColorProperty("St. James Place", "orange", 180, 90, 100, [14, 70, 200, 550, 750, 950]), ChooseField("Community Chest"), ColorProperty("Tennessee Avenue", "orange", 180, 90, 100, [14, 70, 200, 550, 750, 950]), ColorProperty("New York Avenue", "orange", 200, 100, 100, [16, 80, 220, 600, 800, 1000]), DummyField("Free Parking"), ColorProperty("Kentucky Avenue", "red", 220, 110, 150, [18, 90, 250, 700, 875, 1050]), ChooseField("Chance"), ColorProperty("Indiana Avenue", "red", 220, 110, 150, [18, 90, 250, 700, 875, 1050]), ColorProperty("Illinois Avenue", "red", 240, 120, 150, [20, 100, 300, 750, 925, 1100]), Railroad("B. & O. Railroad", 200, 100, [25, 50, 100, 200]), ColorProperty("Atlantic Avenue", "yellow", 260, 130, 150, [22, 110, 330, 800, 975, 1150]), ColorProperty("Ventnor Avenue", "yellow", 260, 130, 150, [22, 110, 330, 800, 975, 1150]), Utility("Water Works", 150, 75, [4, 10]), ColorProperty("Marvin Gardens", "yellow", 280, 140, 150, [24, 120, 360, 850, 1025, 1200]), DummyField("Go To Jail"), ColorProperty("Pacific Avenue", "green", 300, 150, 200, [26, 130, 390, 900, 1100, 1275]), ColorProperty("North Carolina Avenue", "green", 300, 150, 200, [26, 130, 390, 900, 1100, 1275]), ChooseField("Community Chest"), ColorProperty("Pennsylvania Avenue", "green", 320, 160, 200, [28, 150, 450, 1000, 1200, 1400]), Railroad("Short Line", 200, 100, [25, 50, 100, 200]), ChooseField("Chance"), ColorProperty("Park Place", "darkblue", 350, 175, 200, [35, 175, 500, 1100, 1300, 1500]), PayField("Luxury Tax", 100), ColorProperty("Boardwalk", "darkblue", 400, 200, 200, [50, 200, 600, 1400, 1700, 2000])])
p1 = Player("P1", 0, 1500)
p2 = Player("P2", 0, 1500)
p3 = Player("P3", 0, 1500)
p4 = Player("P4", 0, 1500)
g = Game(board=b, players=[p1, p2, p3, p4])
g.start()
