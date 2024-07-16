import tkinter as tk

class Screen:
    def __init__(self,master):
        self.main_screen = master
        self.main_screen.title('Pegasus - Store Front and Stock Management')
        self.main_screen.geometry('350x150')
        #Creating screen elements
        self.label1 = tk.Label(self.main_screen, text="Choose one of the options below:")
        
        selected_opt = tk.StringVar(value=1)

        self.r1 = tk.Radiobutton(
            master_screen,
            text= 'List products and prices',
            value= 1,
            variable=selected_opt
        )   
        self.r2 = tk.Radiobutton(
            master_screen,
            text= 'Include/Exclude/Update an item in your request',
            value= 2,
            variable=selected_opt
        )
        self.r3 = tk.Radiobutton(
            master_screen,
            text= 'Include/Exclude/Update an item in your product list',
            value= 3,
            variable=selected_opt
        )

        #Positioning widgets on screen
        # self.label1.pack(side = tk.LEFT, expand = tk.YES)
        # self.r1.pack(side= tk.LEFT)
        # self.r2.pack(side= tk.LEFT)
        # self.r3.pack(side= tk.LEFT)
        self.label1.place(x = 10,y = 10)
        self.r1.place(x=20, y=30)
        self.r2.place(x=20, y=50)
        self.r3.place(x=20, y=70)

        button = tk.Button(self.main_screen, text="Ok", command= lambda:run_opt(selected_opt, self, product_list))

        button.pack(fill='x', padx=5, pady=5)

def run_opt(opt, root, product_list):
    print(opt.get())
    if opt.get() == '1':
        show_product_list(product_list, root)

#Creating our root interface

master_screen = tk.Tk()

Screen(master_screen)

master_screen.mainloop()