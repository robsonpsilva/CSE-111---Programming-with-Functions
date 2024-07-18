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


global crud_win
global insert_product_window 


def main():
    try:
        #Acquiring product list
        
        product_dict = system_setup()            
        show_main_window(product_dict)
           
    except FileNotFoundError as not_found_err:
        print('Error: missing file')
        print(not_found_err)
            

#GUI section begin ------------------------------------------------------------------
"""
The responsibility of this section of code is to create and manipulate the system GUI.

"""

def show_main_window(product_dict):
    
    #Creating main window
    global root
    root = tk.Tk()
    root.title('Pegasus - Store Front and Stock Management')
    root.geometry('350x180')
    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center')

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

    button1 = ttk.Button(root, text="Ok", command= lambda:run_opt(selected_opt, product_dict))

    button1.pack(fill='x', padx=5, pady=5)

    button2 = ttk.Button(root, text='Close', command=root.destroy)
    button2.pack(fill='x', padx=5, pady=5)

    root.mainloop()

def run_opt(opt, product_dict):
    if opt.get() == '1':
        root.withdraw()
        show_product_list(product_dict)

    elif opt.get() == '2':
        ...

def show_product_list(product_dict):
    #This screen show the product list
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

    #Mounting a list to easy generate a table in screen
    product_list = []
    for pd in product_dict:
        product_list.append(product_dict[pd])

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

    bt_ins_product_list = ttk.Button(frame2, text='Insert', width = 20, command= lambda:ins_new_product(crud_win, product_dict))
    bt_alt_product_list = ttk.Button(frame2, text='Update', width =  20, command= lambda:alt_product(crud_win,product_dict))
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


def ins_new_product(crud_win, product_dict): 
    crud_win.destroy()
    # Creating insert product window
    insert_product_window = tk.Toplevel(root)
    insert_product_window.title('Pegasus - Product list management')
 
    lb1 = ttk.Label(insert_product_window, text="Product ID:")
    lb1.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)

    global product_id_entry
    product_id_entry = ttk.Entry(insert_product_window, width = 20)
    product_id_entry.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

    lb2 = ttk.Label(insert_product_window, text="Product name:")
    lb2.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)

    global product_name_entry
    product_name_entry = ttk.Entry(insert_product_window, width = 50)
    product_name_entry.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5, columnspan=5)

    lb3 = ttk.Label(insert_product_window, text="Quantity:")
    lb3.grid(row=2, column=0, sticky=tk.E, padx=5, pady=5)

    global product_qtd_entry
    product_qtd_entry = ttk.Entry(insert_product_window, width = 20)
    product_qtd_entry.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
    
    btn_close_prod = ttk.Button(insert_product_window, text='Close', width = 20, command = lambda:exit(insert_product_window,product_dict))
    btn_close_prod.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)

    btn_save_prod = ttk.Button(insert_product_window, text='Save', width = 20, command= lambda:save_new_product(product_dict, product_id_entry.get(),product_name_entry.get(), product_qtd_entry.get()))
    btn_save_prod.grid(row=4, column=2, sticky=tk.W, padx=5, pady=5)

    
    root.eval(f'tk::PlaceWindow {str(insert_product_window)} center')


def exit(win, product_dict):
    #Destroy current window
    win.destroy()
    #Show product list and crud window
    show_product_list(product_dict)

def messagebox_manager(code, msg):
    # code = 0 product already exists
    if code == 0:
        messagebox.showwarning('Pegasus', msg)
    elif code == 1:
    # code = 1 product saved with success
        messagebox.showinfo('Pegasus', msg)
    elif code == 2:
    # code = 2 error
        messagebox.showerror('Pegasus', msg)
    # After message return focus to product_id_entry
    product_id_entry.focus()

def insert_product_clear():
    #Cleaning product id entry
    product_id_entry.delete(0,tk.END)
    #Cleaning product name entry
    product_name_entry.delete(0,tk.END)
    #Cleaning product quantity entry
    product_qtd_entry.delete(0, tk.END)
    
def alt_product(crud_win,product_dict):
    crud_win.destroy()
    # Creating insert product window
    alt_product_window = tk.Toplevel(root)
    alt_product_window.title('Pegasus - Product list management')
 
    lb1 = ttk.Label(alt_product_window, text="Product ID:")
    lb1.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)

    global product_id_entry
    product_id_entry = ttk.Entry(alt_product_window, width = 20)
    product_id_entry.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

    lb2 = ttk.Label(alt_product_window, text="Product name:")
    lb2.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)

    global product_name_entry
    product_name_entry = ttk.Entry(alt_product_window, width = 50)
    product_name_entry.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5, columnspan=5)

    lb3 = ttk.Label(alt_product_window, text="Quantity:")
    lb3.grid(row=2, column=0, sticky=tk.E, padx=5, pady=5)

    global product_qtd_entry
    product_qtd_entry = ttk.Entry(alt_product_window, width = 20)
    product_qtd_entry.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
    
    btn_close_prod = ttk.Button(alt_product_window, text='Close', width = 20, command = lambda:exit(alt_product_window, crud_win,product_dict))
    btn_close_prod.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)

    btn_save_prod = ttk.Button(alt_product_window, text='Save', width = 20, command= lambda:save_alt_product(product_dict, product_id_entry.get(),product_name_entry.get(), product_qtd_entry.get()))
    btn_save_prod.grid(row=4, column=2, sticky=tk.W, padx=5, pady=5)

    
    root.eval(f'tk::PlaceWindow {str(alt_product_window)} center')
    
    
#GUI section end ------------------------------------------------------------------


#Functions section begin-----------------------------------------------------------
"""
Functions section
This section contains the functions that perform system activities. 
Such as reading and saving products in the system product list.

"""

#The purpose of this code is load 
#Initial essential data and configuration
def system_setup():
    #Loading product list
    file = path + filename
    products = read_dictionary_from_file(file, key_column_index)
    return products

def read_dictionary_from_file(filename, key_column_index):
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
def save_dictionary_in_file(filename,dict):
    with open(filename, "w") as csv_file:
        for i in dict:
            l = dict[i]
            csv_file.write(f'{l[0]},{l[1]},{l[2]}\n')

def save_new_product(product_dict, id,name,qtd):
    try:
        if id in product_dict:
            code = 0
            msg = f'Product ID {id} already exists'
        else:
            quantity = float(qtd)
            #creating a product list structure
            l = [id,name,qtd]
            #Store the new product in list
            product_dict[id] = l
            #Save new product in file
            file = path + filename
            save_dictionary_in_file(file,product_dict)
            code = 1
            msg = 'Data saved successfully'
            insert_product_clear()
    except ValueError as val_err:
        code = 2
        msg = f'Invalid quantity: {qtd}'
    except FileNotFoundError as file_err:
        code = 2
        msg = f'File {file} not found'
    finally:
        messagebox_manager(code,msg)
        
def save_alt_product(product_dict, id,name,qtd):
    try:
        if id in product_dict:
            quantity = float(qtd)
            #creating a product list structure
            l = [id,name,qtd]
            #Store the product in list
            product_dict[id] = l
             #Save new product in file
            file = path + filename
            save_dictionary_in_file(file,product_dict)
            code = 1
            msg = 'Data saved successfully'
        else:
            code = 0
            msg = f"Product ID {id} doesn't exists"
    
    except ValueError as val_err:
        code = 2
        msg = f'Invalid quantity: {qtd}'
    except FileNotFoundError as file_err:
        code = 2
        msg = f'File {file} not found'
    finally:
        messagebox_manager(code,msg)

#Functions section end----------------------------------------------------------- 

# Call main to start this program.
if __name__ == "__main__":
    main()