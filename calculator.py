import re
from tkinter import *
from tkinter import messagebox


VALID_CHARS = ('0', '1', '2', '3', '4', '5', '6', '7',
               '8', '9', '%', '-', '+', '*', '/', '.')

root = Tk()
root.title('Calculator')

# Change default font size
root.option_add('*Font', 'TkDefaultFont 20')


def validate(inp):
    '''Ensures the input is valid'''
    for char in inp:
        if char not in VALID_CHARS:
            return False
    if re.findall('[-+*/.][*/%]', inp):
        return False
    if re.findall('[-+]{3}', inp):
        return False
    if re.findall('%[%0-9]', inp):
        return False
    if re.findall('[.][-+]', inp) or re.findall('[.][0-9]*[.]', inp):
        return False
    if re.findall('^[*/%]', inp):
        return False
    return True


# Create, configure, and display entry field
e = Entry(root, width=50, borderwidth=5)
reg = root.register(validate)
e.configure(validate='key', vcmd=(reg, '%P'))
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10,)


# Define functions


def evaluate():
    '''Evaluates the current input and returns the result'''
    string = e.get()
    if string == '':
        answer = ''
    else:
        new_string = string.replace('%', '* 0.01')
        answer = eval(new_string)
    return answer


def plusMinusClick():
    '''Switches the input between positive and negative'''
    if e.get() == '':
        e.insert(0, '-')
    elif e.get()[0] == '-':
        new_text = e.get()[1:]
        e.delete(0, END)
        e.insert(0, new_text)
    else:
        e.insert(0, '-')


def sqrtClick():
    '''Evaluate the current input and take the square root'''
    answer = evaluate()
    # Do nothing if there is no input
    if answer == '':
        return
    # Return error if input is negative
    elif answer < 0:
        messagebox.showinfo(
            'Error', 'Cannot take square root of negative number')
    # Otherwise return the answer
    else:
        e.delete(0, END)
        sqrt_answer = answer ** 0.5
        # Convert the float to an integer if it's a whole number
        if sqrt_answer.is_integer():
            e.insert(0, int(sqrt_answer))
        else:
            e.insert(0, sqrt_answer)


def percentClick():
    '''Inserts a % sign at the end of the input'''
    e.insert(END, '%')


def divisionClick():
    '''Inserts a / sign at the end of the input'''
    e.insert(END, '/')


def button_9Click():
    '''Inserts a 9 at the end of the input'''
    e.insert(END, '9')


def button_8Click():
    '''Inserts a 8 at the end of the input'''
    e.insert(END, '8')


def button_7Click():
    '''Inserts a 7 at the end of the input'''
    e.insert(END, '7')


def button_6Click():
    '''Inserts a 6 at the end of the input'''
    e.insert(END, '6')


def button_5Click():
    '''Inserts a 5 at the end of the input'''
    e.insert(END, '5')


def button_4Click():
    '''Inserts a 4 at the end of the input'''
    e.insert(END, '4')


def button_3Click():
    '''Inserts a 3 at the end of the input'''
    e.insert(END, '3')


def button_2Click():
    '''Inserts a 2 at the end of the input'''
    e.insert(END, '2')


def button_1Click():
    '''Inserts a 1 at the end of the input'''
    e.insert(END, '1')


def button_0Click():
    '''Inserts a 0 at the end of the input'''
    e.insert(END, '0')


def button_multClick():
    '''Inserts a * at the end of the input'''
    e.insert(END, '*')


def button_minusClick():
    '''Inserts a - at the end of the input'''
    e.insert(END, '-')


def button_plusClick():
    '''Inserts a + at the end of the input'''
    e.insert(END, '+')


def button_dotClick():
    '''Inserts a . at the end of the input'''
    e.insert(END, '.')


def button_equalsClick():
    '''Evaluates the current expression and displays the result'''
    answer = evaluate()
    e.delete(0, END)
    # Convert floats to integers if they're whole numbers
    if isinstance(answer, float):
        if answer.is_integer():
            e.insert(0, int(answer))
        else:
            e.insert(0, answer)
    else:
        e.insert(0, answer)


def button_clearClick():
    '''Clears the current input'''
    e.delete(0, END)


# Create buttons
button_plus_minus = Button(root, text="+/-", command=plusMinusClick)
button_sqrt = Button(root, text=u"\u221A", command=sqrtClick)
button_percent = Button(root, text=u"\u0025", command=percentClick)
button_division = Button(root, text=u"\u00F7", command=divisionClick)

button_7 = Button(root, text='7', command=button_7Click)
button_8 = Button(root, text='8', command=button_8Click)
button_9 = Button(root, text='9', command=button_9Click)
button_mult = Button(root, text=u"\u00D7", command=button_multClick)

button_4 = Button(root, text='4', command=button_4Click)
button_5 = Button(root, text='5', command=button_5Click)
button_6 = Button(root, text='6', command=button_6Click)
button_minus = Button(root, text='-', command=button_minusClick)

button_1 = Button(root, text='1', command=button_1Click)
button_2 = Button(root, text='2', command=button_2Click)
button_3 = Button(root, text='3', command=button_3Click)
button_plus = Button(root, text='+', command=button_plusClick)

button_0 = Button(root, text='0', command=button_0Click)
button_dot = Button(root, text='.', command=button_dotClick)
button_equals = Button(root, text='=', command=button_equalsClick)
button_clear = Button(root, text='Clear', command=button_clearClick)

# Display buttons
button_plus_minus.grid(row=1, column=0, padx=20, pady=10, sticky=N+S+E+W)
button_sqrt.grid(row=1, column=1, padx=20, pady=10, sticky=N+S+E+W)
button_percent.grid(row=1, column=2, padx=20, pady=10, sticky=N+S+E+W)
button_division.grid(row=1, column=3, padx=20, pady=10, sticky=N+S+E+W)

button_7.grid(row=2, column=0, padx=20, pady=10, sticky=N+S+E+W)
button_8.grid(row=2, column=1, padx=20, pady=10, sticky=N+S+E+W)
button_9.grid(row=2, column=2, padx=20, pady=10, sticky=N+S+E+W)
button_mult.grid(row=2, column=3, padx=20, pady=10, sticky=N+S+E+W)

button_4.grid(row=3, column=0, padx=20, pady=10, sticky=N+S+E+W)
button_5.grid(row=3, column=1, padx=20, pady=10, sticky=N+S+E+W)
button_6.grid(row=3, column=2, padx=20, pady=10, sticky=N+S+E+W)
button_minus.grid(row=3, column=3, padx=20, pady=10, sticky=N+S+E+W)

button_1.grid(row=4, column=0, padx=20, pady=10, sticky=N+S+E+W)
button_2.grid(row=4, column=1, padx=20, pady=10, sticky=N+S+E+W)
button_3.grid(row=4, column=2, padx=20, pady=10, sticky=N+S+E+W)
button_plus.grid(row=4, column=3, padx=20, pady=10, sticky=N+S+E+W)

button_0.grid(row=5, column=0, padx=20, pady=10, sticky=N+S+E+W)
button_dot.grid(row=5, column=1, padx=20, pady=10, sticky=N+S+E+W)
button_equals.grid(row=5, column=2, padx=20, pady=10, sticky=N+S+E+W)
button_clear.grid(row=5, column=3, padx=20, pady=10, sticky=N+S+E+W)


root.mainloop()
