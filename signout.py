import tkinter as tk
import time, sys, random, customtkinter, datetime
from tkinter.ttk import Label
from tkinter.messagebox import showinfo
from CTkMessagebox import CTkMessagebox
from PIL import ImageTk, Image

root = customtkinter.CTk()
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue") # Themes: "blue", "green", "dark-blue"
root.geometry('1000x500')
root.resizable(True, True)
root.title('WMS Sign-Out')


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=1)
root.rowconfigure(7, weight=1)

other = tk.StringVar(root)
name = tk.StringVar(root)
place = tk.StringVar(root)
place.set("Bathroom")


class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()

    def elapsed_time(self):
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        else:
            return 0

    def reset(self):
        self.start_time = None
        self.end_time = None

def write_to_file():
    #print("Saving")
    ct = 0
    SaveName = ""
    Saveplace = ""
    weight_to_file = ""
    global original_color
    global place
    
    #print("Name = ")
    SaveName=str(name.get())
    SaveName = str.title(SaveName)
    #print(SaveName)
                 
    #print("Where = ")
    Saveplace=str(place.get())
    Saveplace=Saveplace.rstrip('\r\n')
    #print(Saveplace)
    
    SaveplaceOther = ''
    if Saveplace == "Other":
        Saveplace = str(other.get())+" (Other)"
    
    stopwatch = Stopwatch()

    if SaveName != "" and SaveName != "Name":
        if Saveplace != str(" (Other)"):
            hs = open("C:/Users/nicos/Documents/wms_sign_out.csv","a") #Laptop
            #hs = open("./wms_sign_out.csv","a") #Replit
            ct = datetime.datetime.now()
            
            hs.write(SaveName)
            hs.write(",")
            
            hs.write(Saveplace)
            hs.write(",")
            
            stopwatch.start()
            hs.write(str(ct))
            hs.write(",")
            
            pop = CTkMessagebox(title="Saved", message=SaveName+', thank you for signing out,\nplease take the pass.\n \nClick the button when you are back.', option_1="I'm back.")
    
            if pop.get()=="I'm back.":
                stopwatch.stop()
                print("name")
                #NameEntry.delete(0, "end")
                #NameEntry.insert(0, "Name")
                #original_color = NameEntry.cget('text_color')
                #NameEntry.configure(text_color='grey') # This is running
                #PlaceHolder(0)
                
            #hs.write(str(ct))
            #hs.write(",")
            total = stopwatch.elapsed_time()
            rounded_total = round(total)
            rounded_total = str(rounded_total)
            hs.write(rounded_total)
    
            hs.write(" \n")
            stopwatch.reset()
            hs.close()
            where_text.focus()
            #placeHolder(0)
            name.set('')
            other.set("")
            #NameEntry.delete(0, "end")
        else:    
            CTkMessagebox(title="Error", message='Please enter a place.', icon="cancel")
    else:            
        CTkMessagebox(title="Error", message='Please enter a name.', icon="cancel")




def on_entry_click(event):
    if NameEntry.get() == "Name":
       NameEntry.delete(0, "end") # delete all the text in the entry
       NameEntry.insert(0, '') #Insert blank for user input 
       NameEntry.configure(text_color=original_color)

def placeHolder(place):
    global original_color
    name.set('')
    name.set("Name")
    original_color = NameEntry.cget('text_color')
    NameEntry.configure(text_color='grey')
    NameEntry.bind('<FocusIn>', on_entry_click)
    #where_text.bind('<FocusIn>', placeHolder)

def reset_name_entry():
    global original_color
    NameEntry.delete(0, tk.END)
    NameEntry.insert(0, "Name")
    original_color = NameEntry.cget('text_color')
    NameEntry.configure(text_color='grey')
    NameEntry.bind('<FocusIn>', on_entry_click)
    
btnSaveToFile = customtkinter.CTkButton(root,
            text = "Sign Out",
            font=("Helvetica", 60),
            command = write_to_file,
            width = 300,
            height = 100)
            
            

btnSaveToFile.grid(row = 6, column = 0, columnspan = 1, rowspan = 1, sticky='w', padx=(25, 0))

        
where_text = customtkinter.CTkLabel(
        root,
        text=("Where are you going:"),
        font=("Helvetica", 40))

where_text.grid(row = 0, column = 0,columnspan = 1,rowspan = 4, sticky='w', padx=(30, 0))

name_text = customtkinter.CTkLabel(
  root,
  text=("Name:"),
  font=("Helvetica", 40))

name_text.grid(row = 0, column = 0,columnspan = 1,rowspan = 1, sticky='nw', padx=(30, 0), pady=(1, 0))

NameEntry = customtkinter.CTkEntry(root,
                     textvariable  = name,
                     font=("Helvetica", 60),
                     width = 300,
                     height = 60
                     )

NameEntry.grid(row = 0,column = 0,columnspan=1,rowspan = 2, sticky='w', padx=(25, 0))


OtherEntry = customtkinter.CTkEntry(root,
                     textvariable  = other,
                     font=("Helvetica", 60),
                     width = 300,
                     height = 60
                     )

OtherEntry.grid(row = 5,column = 0,columnspan=1,rowspan = 1, sticky='nw', padx=(25, 0))

#NameEntry.delete(0, "end")
#NameEntry.insert(0, "Name")
#original_color = NameEntry.cget('text_color')
#NameEntry.configure(text_color='grey')
#NameEntry.bind('<FocusIn>', on_entry_click)
#placeHolder(0)

r1 = customtkinter.CTkRadioButton(root, text='Bathroom', font=("Helvetica", 20), value='Bathroom', variable=place)
r1.grid(row = 2, column = 0, rowspan = 1, columnspan = 1, sticky='w', padx=(40, 0))  # 'w' makes the button stick to the west (left) side of the cell
 

r2 = customtkinter.CTkRadioButton(root, text='Locker', font=("Helvetica", 20), value='Locker', variable=place)
r2.grid(row = 3, column = 0, rowspan = 1, columnspan = 1, sticky='w', padx=(40, 0))  # Added padx=(10, 0) for left-side padding


r3 = customtkinter.CTkRadioButton(root, text='Other:', font=("Helvetica", 20), value='Other', variable=place)
r3.grid(row = 4, column = 0, rowspan = 1, columnspan = 1, sticky='w', padx=(40, 0))  


def adjust_font_size(event=None):
    # Calculate a new font size based on the window width and height
    new_font_size = int((root.winfo_width() + root.winfo_height()) // 50)  # Adjust this formula as needed
    
    # Set the new font size for all relevant widgets
    btnSaveToFile.configure(font=("Helvetica", int(new_font_size // 0.6)))
    where_text.configure(font=("Helvetica", int(new_font_size // 1.5)))
    name_text.configure(font=("Helvetica", int(new_font_size // 1.5)))
    NameEntry.configure(font=("Helvetica", new_font_size))
    OtherEntry.configure(font=("Helvetica", new_font_size))
    r1.configure(font=("Helvetica", new_font_size // 2))
    r2.configure(font=("Helvetica", new_font_size // 2))
    r3.configure(font=("Helvetica", new_font_size // 2))

def my_mainloop():
    print('loop')
    root.after(1000, my_mainloop)
    


adjust_font_size(0)
root.bind("<Configure>", adjust_font_size)

#placeHolder(0)
#print('run')
root.mainloop(
)
  

  

