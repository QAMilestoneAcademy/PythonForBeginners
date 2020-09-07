import tkinter

# Let's create the Tkinter window
window = Tk()

# Then, you will define the size of the window in width(312) and height(324) using the 'geometry' method
window.geometry("312x324")

# In order to prevent the window from getting resized you will call 'resizable' method on the window
window.resizable(0, 0)

#Finally, define the title of the window
window.title("Calculator")

# Let's now define the required functions for the Calculator to function properly.

# 1. First is the button click 'btn_click' function which will continuously update the input field whenever a number is entered or any button is pressed it will act as a button click update.
def btn_click(item):
    global expression
    expression = expression + str(item)
    tkinter.input_text.set(expression)

# 2. Second is the button clear 'btn_clear' function clears the input field or previous calculations using the button "C"
def btn_clear():
    global expression
    expression = ""
    tkinter.input_text.set("")

# 3. Third and the final function is button equal ("=") 'btn_equal' function which will calculate the expression present in input field. For example: User clicks button 2, + and 3 then clicks "=" will result in an output 5.
def btn_equal():
    global expression
    result = str(eval(expression)) # 'eval' function is used for evaluating the string expressions directly
    # you can also implement your own function to evalute the expression istead of 'eval' function
    tkinter.input_text.set(result)
    expression = ""

expression = ""
# In order to get the instance of the input field 'StringVar()' is used
input_text = tkinter.StringVar()

# Once all the functions are defined then comes the main section where you will start defining the structure of the calculator inside the GUI.

# The first thing is to create a frame for the input field
input_frame = tkinter.Frame(window, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
input_frame.pack(side = TOP)
