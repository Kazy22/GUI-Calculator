from tkinter import *

class Calculator:
	def __init__(self, master):
		self.master = master
		self.numbercount = 0
		self.dot_used = False
		self.operator = ""
		self.last_number = 0
		self.check0 = True
		self.screen()
	
	def change_hover_bg(self, button):
		button.config(bg = "#1f1f1f")

	def change_exit_bg(self, button):
		button.config(bg = "black")

	def da(self, e):
		print(e)

	def invalid_(self):
		self.pm.config(state = NORMAL)
		self.div.config(state = NORMAL)
		self.mul.config(state = NORMAL)
		self.min.config(state = NORMAL)
		self.plus.config(state = NORMAL)
		self.equal.config(state = NORMAL)

	def clear_(self):
		if self.entry.get() == "Invalid":
			self.invalid_()
		self.entry.delete(0, END)
		self.entry.insert(0, "0")
		self.numbercount = 0
		self.last_number = 0
		self.dot_used = False
		self.check0 = True

	def invalid(self):
		self.pm.config(state = DISABLED)
		self.div.config(state = DISABLED)
		self.mul.config(state = DISABLED)
		self.min.config(state = DISABLED)
		self.plus.config(state = DISABLED)
		self.equal.config(state = DISABLED)

	def pm_(self):
		current_entry = self.entry.get()
		if current_entry[0] == "-":
			self.entry.delete(0, END)
			self.entry.insert(0, current_entry.replace("-", ""))
			self.numbercount -= 1
		else:
			if self.numbercount >= 10:
				return

			else:
				self.entry.delete(0, END)
				self.entry.insert(0, "-" + current_entry)
				self.numbercount += 1

	def dot_(self):
		self.invalid_()
		if self.entry.get() == "Invalid":
			self.clear_()
			self.invalid()

		if self.dot_used == False:
			if self.numbercount >= 10:
				return

			elif self.numbercount == 9:
				return

			elif self.entry.get() == "0":
				if self.check0 == True:
					self.numbercount += 2

				else:
					self.numbercount += 1

				current_entry = self.entry.get()
				self.entry.delete(0, END)
				self.entry.insert(0, current_entry + ".")
				self.dot_used = True

			elif self.entry.get() == "":
				return

			else:
				self.numbercount += 1
				current_entry = self.entry.get()
				self.entry.delete(0, END)
				self.entry.insert(0, current_entry + ".")
				self.dot_used = True

	def divide(self):
		self.operator = "/"
		self.check0 = False
		try:
			self.last_number = int(self.entry.get())

		except:
			self.last_number = float(self.entry.get())


		self.entry.delete(0, END)
		self.numbercount = 0
		self.dot_used = False

	def multiply(self):
		self.operator = "*"
		self.check0 = False
		try:
			self.last_number = int(self.entry.get())

		except:
			self.last_number = float(self.entry.get())

		self.entry.delete(0, END)
		self.numbercount = 0
		self.dot_used = False

	def minus(self):
		self.operator = "-"
		self.check0 = False
		try:
			self.last_number = int(self.entry.get())

		except:
			self.last_number = float(self.entry.get())

		self.entry.delete(0, END)
		self.numbercount = 0
		self.dot_used = False

	def add(self):
		self.operator = "+"
		self.check0 = False
		try:
			self.last_number = int(self.entry.get())
			
		except:
			self.last_number = float(self.entry.get())

		self.entry.delete(0, END)
		self.numbercount = 0
		self.dot_used = False

	def equal_(self):
		if self.operator == "":
			return

		elif self.operator == "/":
			self.operator == ""
			self.dot_used = False
			try:
				resulttest = self.last_number / float(self.entry.get())
				if resulttest.is_integer() == False:
					result = self.last_number / float(self.entry.get())
					self.entry.delete(0, END)
					self.entry.insert(0, str(result))
					self.numbercount = len(str(self.entry.get()))

				else:
					result = self.last_number / float(self.entry.get())
					result = int(result)
					self.entry.delete(0, END)
					self.entry.insert(0, str(result))
					self.numbercount = len(str(self.entry.get()))

			except:
				self.entry.delete(0, END)
				self.last_number = 0
				self.numbercount = 0
				self.entry.insert(0, "Invalid")
				self.invalid()

		elif self.operator == "*":
			self.operator == ""
			self.dot_used = False
			resulttest = self.last_number * float(self.entry.get())
			if resulttest.is_integer() == False:
				result = self.last_number * float(self.entry.get())
				self.entry.delete(0, END)
				self.entry.insert(0, str(result))
				self.numbercount = len(str(self.entry.get()))

			else:
				result = self.last_number * float(self.entry.get())
				result = int(result)
				self.entry.delete(0, END)
				self.entry.insert(0, str(result))
				self.numbercount = len(str(self.entry.get()))

		elif self.operator == "-":
			self.operator == ""
			self.dot_used = False
			resulttest = self.last_number - float(self.entry.get())

			if resulttest.is_integer() == False:
				result = self.last_number - float(self.entry.get())
				self.entry.delete(0, END)
				self.entry.insert(0, str(result))
				self.numbercount = len(str(self.entry.get()))

			else:
				result = self.last_number - float(self.entry.get())
				result = int(result)
				self.entry.delete(0, END)
				self.entry.insert(0, str(result))
				self.numbercount = len(str(self.entry.get()))

		elif self.operator == "+":
			self.operator = ""
			self.dot_used = False
			resulttest = self.last_number + float(self.entry.get())
			if resulttest.is_integer() == False:
				result = self.last_number + float(self.entry.get())
				self.entry.delete(0, END)
				self.entry.insert(0, str(result))
				self.numbercount = len(str(self.entry.get()))

			else:
				result = self.last_number + float(self.entry.get())
				result = int(result)
				self.entry.delete(0, END)
				self.entry.insert(0, str(result))
				self.numbercount = len(str(self.entry.get()))

	def pressed(self, number):
		if self.entry.get() == "Invalid":
			self.clear_()
			self.invalid_()

		if number == "11" and self.entry.get() != "0":
			self.pm_()

		elif number == "11" and self.entry.get() == "0":
			return

		elif self.numbercount >= 10:
			return

		else:
			if number == "0":
				if self.entry.get() == "0":
					return

				else:
					current_entry = self.entry.get()
					self.entry.delete(0, END)
					self.entry.insert(0, current_entry + number)
					self.numbercount += 1
			elif self.entry.get() == "0":
				self.numbercount = 0
				self.entry.delete(0, END)
				self.pressed(number)

			else:
				current_entry = self.entry.get()
				self.entry.delete(0, END)
				self.entry.insert(0, current_entry + number)
				self.numbercount += 1

	def screen(self):
		# Label
		self.label = Label(self.master, text = "Simple Calculator", bg = "black", fg = "white", font = ("Candara", 15))
		self.label.grid(row = 0, column = 0, sticky = W, padx = 7, columnspan = 4)

		# Buttons
		self.entry = Entry(self.master, bg = "black", fg = "white", bd = 0, font = ("Sans-Bold", 35), justify = "right", width = 10)
		self.entry.insert(END, "0")
		self.entry.bind("<Key>", lambda e: "break")

		self.borderclear= LabelFrame(self.master, bd = 1, bg = "white", relief = FLAT)
		self.clear = Button(self.borderclear, text = "C", bg = "black", fg = "white", font = ("Sans-Bold", 20), width = 3, relief = SUNKEN, command = self.clear_, activebackground = "#1f1f1f", activeforeground = "white")
		self.clear.bind("<Enter>", lambda event, button = self.clear: self.change_hover_bg(button))
		self.clear.bind("<Leave>", lambda event, button = self.clear: self.change_exit_bg(button))

		self.borderpm= LabelFrame(self.master, bd = 1, bg = "white", relief = FLAT)
		self.pm = Button(self.borderpm, text = "+/-", bg = "black", fg = "white", font = ("Sans-Bold", 20), width = 3, relief = SUNKEN, command = lambda: self.pressed("11"), activebackground = "#1f1f1f", activeforeground = "white")
		self.pm.bind("<Enter>", lambda event, button = self.pm: self.change_hover_bg(button))
		self.pm.bind("<Leave>", lambda event, button = self.pm: self.change_exit_bg(button))

		self.borderdiv= LabelFrame(self.master, bd = 1, bg = "white", relief = FLAT)
		self.div = Button(self.borderdiv, text = "/", bg = "black", fg = "white", font = ("Sans-Bold", 20), width = 3, relief = SUNKEN, command = self.divide, activebackground = "#1f1f1f", activeforeground = "white")
		self.div.bind("<Enter>", lambda event, button = self.div: self.change_hover_bg(button))
		self.div.bind("<Leave>", lambda event, button = self.div: self.change_exit_bg(button))

		self.bordermul = LabelFrame(self.master, bd = 1, bg = "white", relief = FLAT)
		self.mul = Button(self.bordermul, text = "*", bg = "black", fg = "white", font = ("Sans-Bold", 20), width = 3, relief = SUNKEN, command = self.multiply, activebackground = "#1f1f1f", activeforeground = "white")
		self.mul.bind("<Enter>", lambda event, button = self.mul: self.change_hover_bg(button))
		self.mul.bind("<Leave>", lambda event, button = self.mul: self.change_exit_bg(button))

		self.bordersev = LabelFrame(self.master, bd = 1, bg = "white", relief = FLAT)
		self.seven = Button(self.bordersev, text = "7", bg = "black", fg = "white", font = ("Sans-Bold", 20), width = 3, relief = SUNKEN, command = lambda: self.pressed("7"), activebackground = "#1f1f1f", activeforeground = "white")
		self.seven.bind("<Enter>", lambda event, button = self.seven: self.change_hover_bg(button))
		self.seven.bind("<Leave>", lambda event, button = self.seven: self.change_exit_bg(button))

		self.bordereight = LabelFrame(self.master, bd = 1, bg = "white", relief = FLAT)
		self.eight = Button(self.bordereight, text = "8", bg = "black", fg = "white", font = ("Sans-Bold", 20), width = 3, relief = SUNKEN, command = lambda: self.pressed("8"), activebackground = "#1f1f1f", activeforeground = "white")
		self.eight.bind("<Enter>", lambda event, button = self.eight: self.change_hover_bg(button))
		self.eight.bind("<Leave>", lambda event, button = self.eight: self.change_exit_bg(button))

		self.bordernine = LabelFrame(self.master, bd = 1, bg = "white", relief = FLAT)
		self.nine = Button(self.bordernine, text = "9", bg = "black", fg = "white", font = ("Sans-Bold", 20), width = 3, relief = SUNKEN, command = lambda: self.pressed("9"), activebackground = "#1f1f1f", activeforeground = "white")
		self.nine.bind("<Enter>", lambda event, button = self.nine: self.change_hover_bg(button))
		self.nine.bind("<Leave>", lambda event, button = self.nine: self.change_exit_bg(button))

		self.bordermin = LabelFrame(self.master, bd = 1, bg = "white", relief = FLAT)
		self.min = Button(self.bordermin, text = "-", bg = "black", fg = "white", font = ("Sans-Bold", 20), width = 3, relief = SUNKEN, command = self.minus, activebackground = "#1f1f1f", activeforeground = "white")
		self.min.bind("<Enter>", lambda event, button = self.min: self.change_hover_bg(button))
		self.min.bind("<Leave>", lambda event, button = self.min: self.change_exit_bg(button))

		self.borderfour = LabelFrame(self.master, bd = 1, bg = "white", relief = FLAT)
		self.four = Button(self.borderfour, text = "4", bg = "black", fg = "white", font = ("Sans-Bold", 20), width = 3, relief = SUNKEN, command = lambda: self.pressed("4"), activebackground = "#1f1f1f", activeforeground = "white")
		self.four.bind("<Enter>", lambda event, button = self.four: self.change_hover_bg(button))
		self.four.bind("<Leave>", lambda event, button = self.four: self.change_exit_bg(button))

		self.borderfive = LabelFrame(self.master, bd = 1, bg = "white", relief = FLAT)
		self.five = Button(self.borderfive, text = "5", bg = "black", fg = "white", font = ("Sans-Bold", 20), width = 3, relief = SUNKEN, command = lambda: self.pressed("5"), activebackground = "#1f1f1f", activeforeground = "white")
		self.five.bind("<Enter>", lambda event, button = self.five: self.change_hover_bg(button))
		self.five.bind("<Leave>", lambda event, button = self.five: self.change_exit_bg(button))

		self.bordersix = LabelFrame(self.master, bd = 1, bg = "white", relief = FLAT)
		self.six = Button(self.bordersix, text = "6", bg = "black", fg = "white", font = ("Sans-Bold", 20), width = 3, relief = SUNKEN, command = lambda: self.pressed("6"), activebackground = "#1f1f1f", activeforeground = "white")
		self.six.bind("<Enter>", lambda event, button = self.six: self.change_hover_bg(button))
		self.six.bind("<Leave>", lambda event, button = self.six: self.change_exit_bg(button))

		self.borderplus = LabelFrame(self.master, bd = 1, bg = "white", relief = FLAT)
		self.plus = Button(self.borderplus, text = "+", bg = "black", fg = "white", font = ("Sans-Bold", 20), width = 3, relief = SUNKEN, command = self.add, activebackground = "#1f1f1f", activeforeground = "white")
		self.plus.bind("<Enter>", lambda event, button = self.plus: self.change_hover_bg(button))
		self.plus.bind("<Leave>", lambda event, button = self.plus: self.change_exit_bg(button))

		self.borderone = LabelFrame(self.master, bd = 1, bg = "white", relief = FLAT)
		self.one = Button(self.borderone, text = "1", bg = "black", fg = "white", font = ("Sans-Bold", 20), width = 3, relief = SUNKEN, command = lambda: self.pressed("1"), activebackground = "#1f1f1f", activeforeground = "white")
		self.one.bind("<Enter>", lambda event, button = self.one: self.change_hover_bg(button))
		self.one.bind("<Leave>", lambda event, button = self.one: self.change_exit_bg(button))

		self.bordertwo = LabelFrame(self.master, bd = 1, bg = "white", relief = FLAT)
		self.two = Button(self.bordertwo, text = "2", bg = "black", fg = "white", font = ("Sans-Bold", 20), width = 3, relief = SUNKEN, command = lambda: self.pressed("2"), activebackground = "#1f1f1f", activeforeground = "white")
		self.two.bind("<Enter>", lambda event, button = self.two: self.change_hover_bg(button))
		self.two.bind("<Leave>", lambda event, button = self.two: self.change_exit_bg(button))

		self.borderthree = LabelFrame(self.master, bd = 1, bg = "white", relief = FLAT)
		self.three = Button(self.borderthree, text = "3", bg = "black", fg = "white", font = ("Sans-Bold", 20), width = 3, relief = SUNKEN, command = lambda: self.pressed("3"), activebackground = "#1f1f1f", activeforeground = "white")
		self.three.bind("<Enter>", lambda event, button = self.three: self.change_hover_bg(button))
		self.three.bind("<Leave>", lambda event, button = self.three: self.change_exit_bg(button))

		self.borderzero = LabelFrame(self.master, bd = 1, bg = "white", relief = FLAT)
		self.zero = Button(self.borderzero, text = "0", bg = "black", fg = "white", font = ("Sans-Bold", 20), width = 7, relief = SUNKEN, command = lambda: self.pressed("0"), activebackground = "#1f1f1f", activeforeground = "white")
		self.zero.bind("<Enter>", lambda event, button = self.zero: self.change_hover_bg(button))
		self.zero.bind("<Leave>", lambda event, button = self.zero: self.change_exit_bg(button))

		self.borderdot = LabelFrame(self.master, bd = 1, bg = "white", relief = FLAT)
		self.dot = Button(self.borderdot, text = ".", bg = "black", fg = "white", font = ("Sans-Bold", 20), width = 3, relief = SUNKEN, command = self.dot_, activebackground = "#1f1f1f", activeforeground = "white")
		self.dot.bind("<Enter>", lambda event, button = self.dot: self.change_hover_bg(button))
		self.dot.bind("<Leave>", lambda event, button = self.dot: self.change_exit_bg(button))

		self.borderequal = LabelFrame(self.master, bd = 1, bg = "white", relief = FLAT)
		self.equal = Button(self.borderequal, text = "=", bg = "black", fg = "white", font = ("Sans-Bold", 20), width = 3, height = 3, relief = SUNKEN, command = self.equal_, activebackground = "#1f1f1f", activeforeground = "white")
		self.equal.bind("<Enter>", lambda event, button = self.equal: self.change_hover_bg(button))
		self.equal.bind("<Leave>", lambda event, button = self.equal: self.change_exit_bg(button))

		self.entry.grid(row = 1, column = 0, columnspan = 4, padx = (0, 7))

		self.borderclear.grid(row = 2, column = 0, sticky = W, padx = (7, 0), pady = (7, 0))
		self.clear.grid(row = 2, column = 0, sticky = W)

		self.borderpm.grid(row = 2, column = 1, sticky = W, padx = (7, 0), pady = (7, 0))
		self.pm.grid(row = 2, column = 1, sticky = W)

		self.borderdiv.grid(row = 2, column = 2, sticky = W, padx = (7, 0), pady = (7, 0))
		self.div.grid(row = 2, column = 2, sticky = W)

		self.bordermul.grid(row = 2, column = 3, sticky = W, padx = (7, 7), pady = (7, 0))
		self.mul.grid(row = 2, column = 3, sticky = W)

		self.bordersev.grid(row = 3, column = 0, sticky = W, padx = (7, 0), pady = (7, 0))
		self.seven.grid(row = 3, column = 0, sticky = W)

		self.bordereight.grid(row = 3, column = 1, sticky = W, padx = (7, 0), pady = (7, 0))
		self.eight.grid(row = 3, column = 1, sticky = W)

		self.bordernine.grid(row = 3, column = 2, sticky = W, padx = (7, 0), pady = (7, 0))
		self.nine.grid(row = 3, column = 2, sticky = W)

		self.bordermin.grid(row = 3, column = 3, sticky = W, padx = (7, 7), pady = (7, 0))
		self.min.grid(row = 3, column = 3, sticky = W)

		self.borderfour.grid(row = 4, column = 0, sticky = W, padx = (7, 0), pady = (7, 0))
		self.four.grid(row = 4, column = 0, sticky = W)

		self.borderfive.grid(row = 4, column = 1, sticky = W, padx = (7, 0), pady = (7, 0))
		self.five.grid(row = 4, column = 1, sticky = W)

		self.bordersix.grid(row = 4, column = 2, sticky = W, padx = (7, 0), pady = (7, 0))
		self.six.grid(row = 4, column = 2, sticky = W)

		self.borderplus.grid(row = 4, column = 3, sticky = W, padx = (7, 7), pady = (7, 0))
		self.plus.grid(row = 4, column = 3, sticky = W)

		self.borderone.grid(row = 5, column = 0, sticky = W, padx = (7, 0), pady = (7, 0))
		self.one.grid(row = 5, column = 0, sticky = W)

		self.bordertwo.grid(row = 5, column = 1, sticky = W, padx = (7, 0), pady = (7, 0))
		self.two.grid(row = 5, column = 1, sticky = W)

		self.borderthree.grid(row = 5, column = 2, sticky = W, padx = (7, 0), pady = (7, 0))
		self.three.grid(row = 5, column = 2, sticky = W)

		self.borderequal.grid(row = 5, column = 3, rowspan = 2, sticky = W, padx = (7, 7), pady = (7, 7))
		self.equal.grid(row = 5, column = 3, sticky = W, ipady = (0.5))

		self.borderzero.grid(row = 6, column = 0, columnspan = 2, sticky = W, padx = (7, 0), pady = (7, 7))
		self.zero.grid(row = 6, column = 0, sticky = W, ipadx = 2)

		self.borderdot.grid(row = 6, column = 2, sticky = W, padx = (7, 0), pady = (7, 7))
		self.dot.grid(row = 6, column = 2, sticky = W)


def main():
	root = Tk()
	root.title("Calculator")
	root.iconbitmap("icon/calculator.ico")
	root.resizable(0, 0)
	root.config(bg = "black")

	Calculator(root)
	root.mainloop()

if __name__ == "__main__":
	main()