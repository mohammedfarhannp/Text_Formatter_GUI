# Import Section
from module.Format import *

# Variables
Window_Size = "500x500"
Window_Title = "Text Formatting Software"

# Window
window = Tk()
window.geometry(Window_Size)
window.title(Window_Title)
window.resizable(False, False)

Input_Area = scrolledtext.ScrolledText(window, wrap=WORD)
Input_Area.place(x=25, y=25, width=450, height=200) # Y end 225

Output_Area = scrolledtext.ScrolledText(window, wrap=WORD)
Output_Area.place(x=25, y=275, width=450, height=200) # Y Begin 275
Output_Area.config(state=DISABLED)

Format_Button = Button(window, text="Format", command=lambda:Format_Text(Output_Area, Input_Area))
Format_Button.place(x=225, y=235, width=50, height=30)

# loop
window.mainloop()
