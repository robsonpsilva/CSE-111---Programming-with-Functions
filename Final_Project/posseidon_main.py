import tkinter as tk

class Screen:
    def __init__(self,master):
        self.main_screen = master
        self.main_screen.title('Pegasus - Store Front and Stock Management')

        #Creating screen elements
        self.label1 = tk.Label(self.main_screen, text="Choose one of the options below")
       
        selected_opt = tk.StringVar()
        self.r = tk.Radiobutton(
            master,
            text= 'List products and prices',
            value= 1,
            variable=selected_opt
        )   
        self.r2 = tk.Radiobutton(
            master,
            text= 'Include/Exclude/Update an item in your request',
            value= 2,
            variable=selected_opt
        )
        self.r3 = tk.Radiobutton(
            master,
            text= 'Include/Exclude/Update an item in your product list',
            value= 3,
            variable=selected_opt
        )

        #Positioning widgets on screen
        self.label1.pack(fill='x', padx=5, pady=5, side=tk.LEFT)
        self.r1.pack(fill='x', padx=20, pady=5, side=tk.LEFT)
        self.r2.pack(fill='x', padx=20, pady=5, side=tk.LEFT)
        self.r3.pack(fill='x', padx=20, pady=5, side=tk.LEFT)

#Creating our root interface

master_screen = tk.Tk()

Screen(master_screen)

master_screen.mainloop()