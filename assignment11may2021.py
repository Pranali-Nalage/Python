#create oa prog to achieve inheritence
class Computer():
	def notepad(self):
		print("write a program here")
class Python(Computer):
	def program(self):
		print("myarr[2,5,3,6]")
c=Python()
c.notepad()
c.program()