# Import Section
from tkinter import *
from tkinter import scrolledtext
from string import ascii_letters

# Functions
def Validate_Key(Key):
    return True
 
def Format_Text(Output_Area, Input_Area):
    Output_Area.config(state=NORMAL)
    Output_Area.delete("1.0", END)
    
    Input_Text = Input_Area.get("1.0", END).strip()
    
    Sentences = Input_Text.split(".")
    New_Sentences = []
    for Sentence in Sentences:
        j = 0
        cap = False
        New = ""
        while j < len(Sentence):
            if(Sentence[j] in ascii_letters and not cap):
                New += Sentence[j].capitalize()
                cap = True
                
            elif (Sentence[j] == "i" and Sentence[j-1] == " " == Sentence[j+1]):
                New += Sentence[j].capitalize()
            
            else:
                New += Sentence[j]
            j+=1
        New_Sentences.append(New)
    
    Input_Text = ".".join(New_Sentences)
    
    i = 0
    while i < len(Input_Text):
        if Input_Text[i:i+2] == "**": # Bold Format
            starting_point = i + 2
            end_point = Input_Text.find("**", starting_point)
            
            if end_point != -1:
                Output_Area.insert(END, Input_Text[i+2:end_point], 'bold')
                i = end_point + 2
            else:
                Output_Area.insert(END, Input_Text[i])
                i = end_point + 1
                
        elif Input_Text[i:i+2] == "__": # Undeline Format
            starting_point = i + 2
            end_point = Input_Text.find("__", starting_point)
            if end_point != -1:
                Output_Area.insert(END, Input_Text[i+2:end_point], 'underline')
                i = end_point + 2
            else:
                Output_Area.insert(END, Input_Text[i])
                i = end_point + 1
            
        elif Input_Text[i:i+2] == "~~": # Italic Format
            starting_point = i + 2
            end_point = Input_Text.find("~~", starting_point)
            if end_point != -1:
                Output_Area.insert(END, Input_Text[i+2:end_point], 'italic')
                i = end_point + 2
            else:
                Output_Area.insert(END, Input_Text[i])
                i = end_point + 1
            
        else:
            Output_Area.insert(END, Input_Text[i])
            i += 1
    
    Output_Area.tag_config('bold', font=('Helvetica', 10, 'bold'))
    Output_Area.tag_config('underline', font=('Helvetica', 10), underline=True)
    Output_Area.tag_config('italic', font=('Helvetica', 10, 'italic'))
    
    Output_Area.config(state=DISABLED)
