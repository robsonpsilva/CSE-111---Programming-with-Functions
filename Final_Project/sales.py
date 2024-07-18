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
global crud_win
global insert_product_window 

#Creating main window
root = tk.Tk()
root.title('Pegasus - Store Front and Stock Management')
root.geometry('350x200')
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')



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
            
    #creating product crud window
    crud_win = tk.Toplevel(root)


    # find total number of rows and
    # columns in list
    total_rows = len(product_list)
    total_columns = len(product_list[0])

    
    
    frame1 = Frame(crud_win)
    frame1.pack(pady=5, padx=10)

    frame2 = Frame(crud_win)
    frame2.pack(pady=5)

    frame3 = Frame(crud_win)
    frame3.pack(pady=5)


    #Creating and populating product list table
    t = Table(frame1)

    bt_ins_product_list = ttk.Button(frame2, text='Insert', width = 20, command=ins_new_product)
    bt_alt_product_list = ttk.Button(frame2, text='Update', width =  20)
    bt_del_product_list = ttk.Button(frame2, text='Delete', width = 20)

          
    #Creating an exit button
    bt_exit = ttk.Button(frame3, text='Close', width= 67, command= lambda:crud_win_exit(crud_win))
       
    bt_ins_product_list.pack(side='left', padx=5)
    bt_alt_product_list.pack(side='left', padx = 5)
    bt_del_product_list.pack(side='left', padx = 5)
   
    bt_exit.pack(side='right', padx = 10)
    #Centralizing the window
    root.eval(f'tk::PlaceWindow {str(crud_win)} center')

def crud_win_exit(w1):
    w1.destroy()
    root.deiconify()


def ins_new_product(): 
    # Creating insert product window
    insert_product_window = tk.Toplevel(root)
    insert_product_window.title('Pegasus - Product list management')
 
    lb1 = ttk.Label(insert_product_window, text="Product ID:")
    lb1.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)

    product_id_entry = ttk.Entry(insert_product_window, width = 20)
    product_id_entry.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

    lb2 = ttk.Label(insert_product_window, text="Product name:")
    lb2.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)

    product_name_entry = ttk.Entry(insert_product_window, width = 50)
    product_name_entry.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5, columnspan=5)

    lb3 = ttk.Label(insert_product_window, text="Quantity:")
    lb3.grid(row=2, column=0, sticky=tk.E, padx=5, pady=5)

    product_qtd_entry = ttk.Entry(insert_product_window, width = 20)
    product_qtd_entry.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
    

    btn_close_prod = ttk.Button(insert_product_window, text='Close', width = 20, command = insert_product_window.destroy)
    btn_close_prod.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)

    btn_save_prod = ttk.Button(insert_product_window, text='Save', width = 20, command= lambda:save_new_product(product_id_entry.get(),product_name_entry.get(), product_qtd_entry.get()))
    btn_save_prod.grid(row=4, column=2, sticky=tk.W, padx=5, pady=5)

    root.eval(f'tk::PlaceWindow {str(insert_product_window)} center')

def save_new_product(id,name,qtd):
    try:
        quantity = float(qtd)
    except ValueError as val_err:
        messagebox.showerror('Pegasus', f'Invalid quantity: {qtd}')
 

# Call main to start this program.
if __name__ == "__main__":
    main()