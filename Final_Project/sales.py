import csv
import tkinter as tk
from tkinter import ttk
from tkinter import *
from datetime import datetime
from tabulate import tabulate
from tkinter import messagebox

key_column_index = 0
filename = 'products.csv'
path = 'Final_Project/'

global root
global second_win
global w1

root = tk.Tk()
second_win = tk.Toplevel(root)

def main():
    try:
        #Acquiring product list
        product_list = []
        product_dict = system_setup()

        for pd in product_dict:
            product_list.append(product_dict[pd])    
        show_initial_screen(product_list)
           
    except FileNotFoundError as not_found_err:
        print('Error: missing file')
        print(not_found_err)
            

#The purpose of this code is load 
#Initial essential data and configuration
def system_setup():
    file = path + filename
    products = read_dictionary(file, key_column_index)
    return products

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}
    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:
        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)
        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)
        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:
            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:
                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[key_column_index]
                # Store the data from the current
                # row into the dictionary.
                dictionary[key] = row_list
    # Return the dictionary.
    return dictionary


def show_initial_screen(product_list):
    
    #This function is responsible to mount the initial screen
    
    
    
    root.title('Pegasus - Store Front and Stock Management')
    root.geometry('350x200')
    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center')


    selected_opt = tk.StringVar(value=1)

    label = ttk.Label(text="Choose one of the options below")
    label.pack(fill='x', padx=5, pady=5)

    r = ttk.Radiobutton(
        root,
        text= 'List products, Include/Exclude/Update an item in your product list',
        value= 1,
        variable=selected_opt
    )
    r.pack(fill='x', padx=20, pady=5)

    r = ttk.Radiobutton(
        root,
        text= 'Include/Exclude/Update an item in your request',
        value= 2,
        variable=selected_opt
    )
    r.pack(fill='x', padx=20, pady=5)

    button1 = ttk.Button(root, text="Ok", command= lambda:run_opt(selected_opt, product_list))

    button1.pack(fill='x', padx=5, pady=5)

    button2 = ttk.Button(root, text='Close', command=root.destroy)
    button2.pack(fill='x', padx=5, pady=5)

    root.mainloop()

def run_opt(opt, product_list):
    if opt.get() == '1':
        root.withdraw()
        show_product_list(product_list)

    elif opt.get() == '2':
        ...

def show_product_list(product_list):
    #This screen show the product screen
    class Table:
        def __init__(self,root):
             
            # code for creating table
            for i in range(total_rows):
                for j in range(total_columns):
                    
                    self.e = Entry(root, width=20, fg='blue',
                                font=('Arial',16,'bold'))
                    
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, product_list[i][j])
            
  
    
    # find total number of rows and
    # columns in list
    total_rows = len(product_list)
    total_columns = len(product_list[0])

    frame1 = Frame(second_win)
    frame1.pack(pady=5, padx=10)

    frame2 = Frame(second_win)
    frame2.pack(pady=5)

    frame3 = Frame(second_win)
    frame3.pack(pady=5)

    #Creating and populating product list table
    t = Table(frame1)

    bt_ins_product_list = ttk.Button(frame2, text='Insert', width = 20, command=ins_new_product)
    bt_alt_product_list = ttk.Button(frame2, text='Update', width =  20)
    bt_del_product_list = ttk.Button(frame2, text='Delete', width = 20)

          
    #Creating an exit button
    bt_exit = ttk.Button(frame3, text='Close', width= 67, command=second_win_exit)
       
    bt_ins_product_list.pack(side='left', padx=5)
    bt_alt_product_list.pack(side='left', padx = 5)
    bt_del_product_list.pack(side='left', padx = 5)
   
    bt_exit.pack(side='right', padx = 10)
 

    #Centralizing the window
    root.eval(f'tk::PlaceWindow {str(second_win)} center')
def second_win_exit():
    second_win.destroy()
    root.deiconify()


def ins_new_product():
    create_product_crud_window()

def create_product_crud_window():
    # Creating second window
    w1 = tk.Tk()
    w1.title('Pegasus - Product list management')
    w1.eval('tk::PlaceWindow . center')


# Call main to start this program.
if __name__ == "__main__":
    main()