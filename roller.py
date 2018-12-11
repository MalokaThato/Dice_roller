# Graphics program to roll a pair of dice. Uses custom widgets
# Button and DieView

from random import randrange
from graphics import *

from button import Button
from dieview import DieView
from msdie import MSdie

def main():

	# create the application window
	win = GraphWin("Dice Roller", 550,550)
	win.setCoords(0,0,10,10)
	win.setBackground("green2")

	#die value holders
	die1_value = 0
	die2_value = 0
	die3_value = 0
	die4_value = 0
	die5_value = 0
	amount = 100.00
	# draw the interface widgets

	roll_btn = Button(win, Point(4,2), 3,2, "Play")
	exit_game = Button(win, Point(8,2),3,2, "Exit")

	amount_Label = Text(Point(5, 9), "Amount: R " + str(amount))
	amount_Label.draw(win)

	die1 = DieView(win, Point(2,5), 1.5)

	die2 = DieView(win, Point(8,5), 1.5)

	die3 = DieView(win, Point(2,7), 1.5)

	die4 = DieView(win, Point(8,7), 1.5)

	die5 = DieView(win, Point(5,6), 1.5)

	# event loop
	while True:
		p = win.getMouse()
		print(p.x)
		if roll_btn.clicked(p):
			die1.setValue(MSdie(6).roll())
			die2.setValue(MSdie(6).roll())
			die3.setValue(MSdie(6).roll())
			die4.setValue(MSdie(6).roll())
			die5.setValue(MSdie(6).roll())
			die1_value = die1.die_Number
			die2_value = die2.die_Number
			die3_value = die3.die_Number
			die4_value = die4.die_Number
			die5_value = die5.die_Number

			#amount_Label.setText(str(die1.die_Number))

		elif exit_game.clicked(p):
			break
		else:
			print("hello")

		count = number_Of_Pairs("hello",die1_value, die2_value, die3_value, die4_value, die5_value)

		if count == "rule1":
			amount += 5
			amount_Label.setText("Amount:R " + str(amount))
			print("Yes")

		elif count == "rule2":
			amount += 8
			amount_Label.setText("Amount:R " + str(amount))

		elif count == "rule3":
			amount += 12
			amount_Label.setText("Amount:R " + str(amount))

		elif count == "rule4":
			amount += 15
			amount_Label.setText("Amount:R " + str(amount))

		elif count == "rule5":
			amount += 20
			amount_Label.setText("Amount:R " + str(amount))

		elif count == "rule6":
			amount += 30
			amount_Label.setText("Amount:R " + str(amount))


		else:
			amount -= 10
			amount_Label.setText("Amount:R " + str(amount))


	# close the window
	win.close()


def number_Of_Pairs(self,*kwargs):

	outer_count = 0
	skeep_count_lst = []
	inner_count = 0
	step_count = 0

	lis1 = [1,2,3,4,5]
	lis2 = [2,3,4,5,6]

	die_check_count = 0

	if kwargs == lis1 or kwargs == lis2:
		return "rule5"
	else:

		while die_check_count < 5:
			count = kwargs.count(kwargs[die_check_count])
			if count == 5 or count == 4:
				return "rule6"
			elif count == 4:
				return "rule4"
			elif count == 3:
				for inner_count in kwargs:
					if kwargs[die_check_count] != inner_count:
						skeep_count_lst.append(inner_count)
						print(skeep_count_lst)

				if skeep_count_lst[0] == skeep_count_lst[1]:

					return "rule3"
				else:
					return "rule2"

			elif count == 2:
				return "rule1"





			die_check_count += 1

	return "rule0"



	#return pair_count




main()
