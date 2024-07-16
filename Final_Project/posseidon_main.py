import tkinter as tk

class Screen:
    def __init__(self,master):
       self.main_screen = master
       self.main_screen.title('Pegasus - Store Front and Stock Management')
       self.label = tk.Label(self.main_screen, text="Choose one of the options below")
       self.label.pack(fill='x', padx=5, pady=5)

#Creating our root interface

master_screen = tk.Tk()

Screen(master_screen)

master_screen.mainloop()