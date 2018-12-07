from graphics import *
import random

class DieView:
	"""DieView is a widget that displays a graphical representation of a standard six-sided die."""


	def __init__(self, win, center, size):
		""" create a view of a die e.g: d1 = DieView (myWin, Point(40,50), 20).This creates a die centered at (40,50) with length 20. """

	# define standard values for drawing the die
		self.win = win 				#for drawing the pips
		self.background = "white"	#colour of die face
		self.foreground = "black"	#colour of pips
		self.psize = 0.1 * size 	#radius of each pip
		hsize = size/2				#half the size of the die
		offset = 0.6 * hsize		#distance from centre to outer pips

	# create a square for the face
		self.width = size/2
		self.height = size/2

		centerX = center.getX()
		centerY = center.getY()

		self.x1 = centerX - self.width
		self.x2 = centerX + self.width
		self.y1 = centerY - self.height
		self.y2 = centerY + self.height

		self.rect = Rectangle(Point(self.x1, self.y1), Point(self.x2, self.y2))
		self.rect.setFill(self.background)
		self.rect.draw(win)

	# create 7 circles for standard pip locations
		self.pip1 = self.__makePip(centerX - offset, centerY - offset)
		self.pip2 = self.__makePip(centerX - offset, centerY)
		self.pip3 = self.__makePip(centerX - offset, centerY + offset)
		self.pip4 = self.__makePip(centerX + offset, centerY + offset)
		self.pip5 = self.__makePip(centerX + offset, centerY)
		self.pip6 = self.__makePip(centerX + offset, centerY - offset)
		self.pip7 = self.__makePip(centerX, centerY)


	# Draw an initial value

		self.setValue(random.randint(1,6))

	def __makePip(self, x, y):
		""" Internal helper method to draw a pip at (x,y)"""
		#CODE
		pip = Circle(Point(x,y), self.psize)
		pip.setFill(self.background)
		pip.setOutline(self.background)
		pip.draw(self.win)
		return pip


	def setValue(self, value):
		"""Set this die to display value. """

		self.pip1.setFill(self.background)
		self.pip2.setFill(self.background)
		self.pip3.setFill(self.background)
		self.pip4.setFill(self.background)
		self.pip5.setFill(self.background)
		self.pip6.setFill(self.background)
		self.pip7.setFill(self.background)

		# turn correct pips on

		if value == 1:
			self.pip7.setFill(self.foreground)
		elif value == 2:
			self.pip1.setFill(self.foreground)
			self.pip4.setFill(self.foreground)
		elif value == 3:
			self.pip1.setFill(self.foreground)
			self.pip4.setFill(self.foreground)
			self.pip7.setFill(self.foreground)
		elif value == 4:
			self.pip1.setFill(self.foreground)
			self.pip3.setFill(self.foreground)
			self.pip4.setFill(self.foreground)
			self.pip6.setFill(self.foreground)
		elif value == 5:
			self.pip1.setFill(self.foreground)
			self.pip3.setFill(self.foreground)
			self.pip4.setFill(self.foreground)
			self.pip6.setFill(self.foreground)
			self.pip7.setFill(self.foreground)
		elif value == 6:
			self.pip1.setFill(self.foreground)
			self.pip3.setFill(self.foreground)
			self.pip4.setFill(self.foreground)
			self.pip6.setFill(self.foreground)
			self.pip2.setFill(self.foreground)
			self.pip5.setFill(self.foreground)

		#turn all pips off

		# turn correct pips on
