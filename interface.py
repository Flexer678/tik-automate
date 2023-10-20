

import tkinter as tk
from tkinter import DoubleVar, Scale, ttk

from botactions import Tiktokbot
#from botactions import Tiktokbot 


class Interface():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tik automate")
        self.root.geometry("300x300")
        self.root.iconbitmap('logo.ico')
        self.root.resizable(width=False, height=False)
        
        self.directory_entry = tk.StringVar()
        Page(self.root)
       
        ttk.Button(self.root,text="Execute Program",padding=2,command=self.run).pack(pady=10, expand=False, fill=None)
        #ttk.Button(self.root,text="End Program",padding=2,command=self.stop).pack(pady=10, expand=False, fill=None)
        
        self.root.mainloop()
    
    def run(self):
        #C:/Users/user/AppData/Local/Google/Chrome/User Data
        #
        #
        
        scrolls = scrollinput.get_scrollvalue
        #print("the scorll value is ", scrollinput.get_scrollvalue)
        directory = directory_1.get_directory
        profile = directory_1.get_profile
        global bot
        bot = Tiktokbot(email="",password="", profile=profile, directory=directory)
        bot.autoscroll(times=scrolls, mute=True)
        
    
    def stop(self):
        #not running cus of global stuff, als it cancels the autoscroll when clicked
        #so threading might be needed
        bot.quit_bot
        
        
    


class Page(ttk.Frame):
    def __init__(self, root, ) : 
        self.tab1 = ttk.Frame(root, width= 100, height=50)
        
        Accounts(self.tab1,)
        global scrollinput
        scrollinput = ScrollInputBox(self.tab1)
        
        self.tab1.pack( expand=True, fill="both")
        
        
        
        
        
        
class Accounts():
    def __init__(self, root) :
        
        
        
            self.tabControll = ttk.Notebook(root, width=300, height= 100)
        
            global directory_1

        
            self.tab1 = ttk.Frame(self.tabControll, width= 100, height=50)
           
                   
           
           
            
            
            directory_1 =DirectoryEntry(self.tab1)
           
            
            self.tabControll.add(self.tab1, text= "account 1")
            #self.tab1.pack(expand=True,)
           
            self.tabControll.grid(row=0, column=0)
           
    
           
  
        
    def get_dir(self):
        self.entry1 = tk.Entry(self.tab1,)
        self.entry1.pack()
        
        
        

class AccountEntry(ttk.Frame):
    def __init__(self, root):
       # super().__init__(parent)
      
        
        
        ttk.Button(root, command=self.username, text="r").grid(row=5, column=0)
    
    
    
   
   #to get a var in the init method





class DirectoryEntry(ttk.Frame):
    def __init__(self,root ):
        ttk.Label(root, text = "chrome Directory").place(relx=0.3, rely=0.3 , anchor="center")
        self.directory =ttk.Entry(root, width=100)
        self.directory.place(relx=0.3, rely=0.5 , anchor="center", width=100)
        
        ttk.Label(root, text = "Profile").place(relx=0.7, rely=0.3 , anchor="center")
        self.profile =ttk.Entry(root, width=100)
        self.profile.place(relx=0.7, rely=0.5 , anchor="center", width=100)
    
    @property
    def get_directory(self):
        return self.directory.get()
    @property
    def get_profile(self):
        return self.profile.get()



        

class ScrollInputBox():
    def __init__(self, root,):
        
        
        self.text= "Scroll for "
        ttk.Label(root, text = self.text).grid(row=2, column= 0)
        
        self.scroll  = tk.Scale(root,orient="horizontal",from_=1,to=80, showvalue=1, command=self.change_scrollvalue)
        self.scrollvalue = self.scroll.get()
        self.scroll.grid(row=3, column=0,)
    

    @property
    def get_scrollvalue(self):
        return self.scrollvalue
    

   
    def change_scrollvalue(self,var):
        self.scrollvalue = self.scroll.get()
        #print(self.get_scrollvalue)
        
        

Interface()

        






#https://stackoverflow.com/questions/9355742/python-tkinter-button-entry-combination





#https://stackoverflow.com/questions/9355742/python-tkinter-button-entry-combination
