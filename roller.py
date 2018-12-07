# Graphics program to roll a pair of dice. Uses custom widgets
# Button and DieView

from random import randrange
from graphics import GraphWin, Point

from button import Button
from dieview import DieView
from msdie import MSdie

def main():

	# create the application window
	win = GraphWin("Dice Roller")
	win.setCoords(0,0,10,10)
	win.setBackground("green2")

	# draw the interface widgets

	roll_btn = Button(win, Point(4,2), 3,2, "Play")
	exit_game = Button(win, Point(8,2),3,2, "Exit")

	die1 = DieView(win, Point(3,6), 3)

	# event loop
	while True:
		if roll_btn.clicked(win.getMouse()):
			die1.setValue(MSdie(6).roll())

		elif exit_game.clicked(win.getMouse()):
			break
		else:
			print("hello")

	# close the window
	win.close()

main()
