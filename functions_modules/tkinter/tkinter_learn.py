# https://www.datacamp.com/community/tutorials/gui-tkinter-python?utm_source=adwords_ppc&utm_campaignid=898687156&utm_adgroupid=48947256715&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=332602034352&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=1000013&gclid=Cj0KCQjw7sz6BRDYARIsAPHzrNJbhmSzRzhBY1WontQSbwuzz8FgU--m_zXWPFY8NU9_Q5oGmYH4ji0aAmmcEALw_wcB

# Create window

# import tkinter
#
# window = tkinter.Tk()
# # to rename the title of the window
# window.title("GUI")
#Create Label
# # pack is used to show the object in the window
# label = tkinter.Label(window, text = "Welcome to DataCamp's Tutorial on Tkinter!")
# label.pack()
# window.mainloop()
#Create Button

# import tkinter
# window = tkinter.Tk()
# window.title("Button GUI")
# button_widget = tkinter.Button(window,text="Welcome to DataCamp's Tutorial on Tkinter")
# button_widget.pack()
# tkinter.mainloop()

#
# To arrange the layout in the window, you will use a Frame widget class. Let's create a simple program to see how the Frame works.
#
# You will define two frames - top and bottom with the help of the pack class. The Frame class will help in creating a division between the window. Basically, a single-window will be replicated twice as top and bottom in the form of a Frame.
#
# Finally, you will create four buttons in the window, two for each frame. You can name and color your buttons as you like as a parameter.
#
# import tkinter
#
# # Let's create the Tkinter window.
# window = tkinter.Tk()
# window.title("GUI")
#
# # You will first create a division with the help of Frame class and align them on TOP and BOTTOM with pack() method.
# top_frame = tkinter.Frame(window).pack()
# bottom_frame = tkinter.Frame(window).pack(side = "bottom")
#
# # Once the frames are created then you are all set to add widgets in both the frames.
# btn1 = tkinter.Button(top_frame, text = "Button1", fg = "red").pack() #'fg or foreground' is for coloring the contents (buttons)
#
# btn2 = tkinter.Button(top_frame, text = "Button2", fg = "green").pack()
#
# btn3 = tkinter.Button(bottom_frame, text = "Button3", fg = "purple").pack(side = "left") #'side' is used to left or right align the widgets
#
# btn4 = tkinter.Button(bottom_frame, text = "Button4", fg = "orange").pack(side = "left")
#
# window.mainloop()


# import tkinter
# from tkinter import *
# top = tkinter.Tk()
# CheckVar1 = IntVar()
# CheckVar2 = IntVar()
# tkinter.Checkbutton(top, text = "Machine Learning",variable = CheckVar1,onvalue = 1, offvalue=0).grid(row=0,sticky=W)
# tkinter.Checkbutton(top, text = "Deep Learning", variable = CheckVar2, onvalue = 0, offvalue =1).grid(row=1,sticky=W)
# top.mainloop()

import tkinter
# Let's create the Tkinter window
window = tkinter.Tk()
window.title("GUI")

# You will create two text labels namely 'username' and 'password' and and two input labels for them

tkinter.Label(window, text = "Username").grid(row = 0) #'username' is placed on position 00 (row - 0 and column - 0)

# 'Entry' class is used to display the input-field for 'username' text label
tkinter.Entry(window).grid(row = 0, column = 1) # first input-field is placed on position 01 (row - 0 and column - 1)

tkinter.Label(window, text = "Password").grid(row = 1) #'password' is placed on position 10 (row - 1 and column - 0)

tkinter.Entry(window).grid(row = 1, column = 1) #second input-field is placed on position 11 (row - 1 and column - 1)

# 'Checkbutton' class is for creating a checkbutton which will take a 'columnspan' of width two (covers two columns)
tkinter.Checkbutton(window, text = "Keep Me Logged In").grid(columnspan = 2)

window.mainloop()