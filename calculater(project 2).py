from tkinter import *

# setting the screen
root = Tk()
root.title('My calculater')



# getting user entry
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# defing everything
def Button_Clicker(number):
	new_number = e.get() + str(number)
	e.delete(0, END)
	e.insert(0, new_number)

def Button_Clear():
	e.delete(0, END)

def Button_Add(first_number):
	global f_num
	global math
	math = "addition"
	f_num = first_number
	#e.insert(0, first_number)
	e.delete(0, END)

def Button_Subtract(first_number):
	global f_num
	global math
	math = "subtraction"
	f_num = first_number
	#e.insert(0, first_number)
	e.delete(0, END)


def Button_Equal(second_number):
	num_1 = f_num
	if math == "addition":
		e.delete(0, END)
		e.insert(0, int(num_1) + int(second_number))
	if math == "subtraction":
		e.delete(0, END)
		e.insert(0, int(num_1) - int(second_number))
	if math == "multiplication":
		e.delete(0, END)
		e.insert(0, int(num_1) * int(second_number))
	if math == "division":
		e.delete(0, END)
		e.insert(0, int(num_1) / int(second_number))

# making all the buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: Button_Clicker(1),bg="green")
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: Button_Clicker(2),bg="green")
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: Button_Clicker(3),bg="green")
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: Button_Clicker(4),bg="green")
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: Button_Clicker(5),bg="green")
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: Button_Clicker(6),bg="green")
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: Button_Clicker(7),bg="green")
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: Button_Clicker(8),bg="green")
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: Button_Clicker(9),bg="green")
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: Button_Clicker(0),bg="green")
button_clear = Button(root, text="Clear", padx=79, pady=20, command=Button_Clear, bg="#145FDA")
button_add = Button(root, text="+", padx=39, pady=20, command=lambda: Button_Add(e.get()),bg="#DA148C")
button_equal = Button(root, text="=", padx=91, pady=20, command=lambda: Button_Equal(e.get()), bg="#14DAC8")

# displaying them on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)

button_equal.grid(row=5, column=1, columnspan=2)


root.mainloop()