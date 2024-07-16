import tkinter as tk

class Screen:
    def __init__(self,master):
       self.main_screen = master
       self.main_screen.title('Pegasus - Store Front and Stock Management')

#Creating our root interface

master_screen = tk.Tk()

Screen(master_screen)

master_screen.mainloop()