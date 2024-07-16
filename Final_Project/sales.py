import csv
import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
from datetime import datetime
from tabulate import tabulate
from tkinter import messagebox

key_column_index = 0
filename = 'products.csv'
path = 'Final_Project/'




def main():
    try:
        #Acquiring product list
        product_list = []
        product_dict = system_setup()
        for pd in product_dict:
            product_list.append(product_dict[pd])    
        show_initial_screen(product_list)
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Choose one of the options below:')
        print('Type 1 to list products and prices')
        print('Type 2 to include/exclude/update an item in your request')
        print('Type 3 to include/exclude/update an item in product list')
        print('Type 0 to exit program')
        option = input("Type your option:")
        if option == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            prod_table = set_product_table(product_dict)
            print(prod_table)
            input('Press any key to continue.')
        
        elif option == '2':
            ...
        elif option == '3':
            ...
        elif option == '0':
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            input('Input error, press any key to continue.')
        """
    
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

def set_product_table(product_dict):
    #Formating headers
    dados = [['Product id','Name','Price']]
    for i in product_dict:
        item = product_dict[i]
        dados.append([i,item[1], item[2]])

    return tabulate(dados,headers='firstrow',tablefmt='grid') 

def show_initial_screen(product_list):
    root = tk.Tk()
    root.title('Pegasus - Store Front and Stock Management')
    root.geometry('350x200')
    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center')
    selected_opt = tk.StringVar()
    label = ttk.Label(text="Choose one of the options below")
    label.pack(fill='x', padx=5, pady=5)

    r = ttk.Radiobutton(
        root,
        text= 'List products and prices',
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

    r = ttk.Radiobutton(
        root,
        text= 'Include/Exclude/Update an item in your product list',
        value= 3,
        variable=selected_opt
    )
    r.pack(fill='x', padx=20, pady=5)

    button = ttk.Button(root, text="Ok", command= lambda:run_opt(selected_opt, root, product_list))

    button.pack(fill='x', padx=5, pady=5)

    root.mainloop()

def run_opt(opt, root, product_list):
    print(opt.get())
    if opt.get() == '1':
        show_product_list(product_list, root)
    
def show_product_list(product_list, root):
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

    
    # Ceeating second window
    second_win = tk.Toplevel(root)

    #Creating product list table
    t = Table(second_win)

    #Centralizing the window
    root.eval(f'tk::PlaceWindow {str(second_win)} center')
    
    

# Call main to start this program.
if __name__ == "__main__":
    main()