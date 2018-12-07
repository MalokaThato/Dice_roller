from graphics import *


class Button:
	""" A button is a labeled rectangle in a window. It is activated or deactivated
	with the activate() and deactivate() methods. The clicked (p) method returns
	true if the button is active and p is inside it. """

	activate = True
	deactivated = False
	label = ""
	Button = ""




	def __init__ (self, win, center, width, height, label):
		"""" creates a rectangualr button, eg: qp = Button (myWin, centerPoint, width, height, 'quit')"""

		self.width = width/2
		self.height = height/2

		centerX = center.getX()
		centerY = center.getY()

		self.x1 = centerX - self.width
		self.x2 = centerX + self.width
		self.y1 = centerY - self.height
		self.y2 = centerY + self.height

		self.Button = Rectangle(Point(self.x1, self.y1), Point(self.x2, self.y2))
		self.Button.setFill("gray")
		#btn_label = Text(Point(self.Button.getCenter().x,self.Button.getCenter().y))
		self.Button.draw(win)
		self.label = Text(center, label)
		self.label.draw(win)


	#set attributes here

	def clicked(self, p):
		"""returns true if the button active and p is inside"""
		left_side = self.Button.getP1()
		right_side = self.Button.getP2()
		if self.activate == True:
			print("hello")
			return left_side.x <= p.x <= right_side.x and left_side.y <= p.y <= right_side.y

		else:
			return True



	#CODE

	def getLabel(self):
		"""returns the label string of the button"""
		return self.label

	#CODE

	def activate(self):
		"""Sets this button to 'active'"""
		self.activate = True

	#CODE

	def deactivate (self):
		"""Sets this button to 'active'"""
		self.activated = False

	#CODE
