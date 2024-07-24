import csv #We use this library to be able to import and manipulate CSV files.

import tkinter as tk #We use tkinter to generate the graphical interface
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

key_column_index = 0
filename = 'products.csv'
filename_request = 'request.csv'
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
            

#Creating main window

def show_main_window(product_dict):
    
    """

        This function works mainly 
        with creating the main screen 
        and associating functions with 
        the two-button click event.

    """
    #Start of creating the home/main screen ----------------------------------------------------
    global root
    root = tk.Tk()
    root.title('Pegasus - Store Front and Stock Management')
    root.geometry('350x180')
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

    #We insert two buttons (button1 and button2) below and associate functions, operations to be executed 
    #once they are clicked.

    #We associate the callback function run_opt(selected_opt, product_dict) that checks which option was
    #selected on the screen, there is a radiobutton, and based on this information selects whether we
    #will proceed to product or request management.
    button1 = ttk.Button(root, text="Ok", command= lambda:run_opt(selected_opt, product_dict))

    button1.pack(fill='x', padx=5, pady=5)

    #To close the main window and the application, we call the native destroy function, below.
    button2 = ttk.Button(root, text='Close', command=root.destroy)
    button2.pack(fill='x', padx=5, pady=5)
    #End of creating the home/main screen -----------------------------------------------------

    root.mainloop() #Puting window to run.

def run_opt(opt, product_dict):
    if opt.get() == '1':
        root.withdraw()
        show_product_list(product_dict)

    elif opt.get() == '2':
        root.withdraw()
        request_window(product_dict)

#Product Management Section Begin ------------------------------------------------
"""
This section contains the graphical interface and functions that manage inventory

"""


def show_product_list(product_dict):

    """

        This function creates the input screen for managing the product list.
        It manages inclusion, deletion and modification of the list.

    """

    #The Table class creates and populates a table where our product 
    #list is displayed.
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

    global total_rows
    global total_columns
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

    #At this point we associate functions that will
    #handle the insertion, alteration and deletion 
    #flows of items in the product list.
    bt_ins_product_list = ttk.Button(frame2, text='Insert', width = 20, command= lambda:ins_new_product(crud_win, product_dict))
    bt_alt_product_list = ttk.Button(frame2, text='Update', width =  20, command= lambda:alt_product(crud_win,product_dict))
    bt_del_product_list = ttk.Button(frame2, text='Delete', width = 20, command= lambda:del_product(crud_win,product_dict))

          
    #Creating an exit button
    #The crud_win_exit function associated with this button
    #not only closes the current window, it also shows the 
    #previous one.
    bt_exit = ttk.Button(frame3, text='Close', width= 67, command= lambda:crud_win_exit(crud_win))
       
    bt_ins_product_list.pack(side='left', padx=5)
    bt_alt_product_list.pack(side='left', padx = 5)
    bt_del_product_list.pack(side='left', padx = 5)
   
    bt_exit.pack(side='right', padx = 10)
    #Centralizing the window
    root.eval(f'tk::PlaceWindow {str(crud_win)} center')

def crud_win_exit(w1):
    """
        The crud_win_exit function closes the window 
        received as a parameter and redisplays the 
        previous one.
    """
    w1.destroy()
    root.deiconify()


def ins_new_product(crud_win, product_dict): 
    crud_win.destroy()

    """
        This function creates the new product insertion window, 
        and associates the save_new_product(...) function with
        the btn_save_prod button, whose responsibility is to insert
        a new item into the product list.
    """
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

    lb3 = ttk.Label(insert_product_window, text="Price:")
    lb3.grid(row=2, column=0, sticky=tk.E, padx=5, pady=5)

    global product_qtd_entry
    product_qtd_entry = ttk.Entry(insert_product_window, width = 20)
    product_qtd_entry.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
    
    btn_close_prod = ttk.Button(insert_product_window, text='Close', width = 20, command = lambda:exit(insert_product_window,product_dict))
    btn_close_prod.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)

    btn_save_prod = ttk.Button(insert_product_window, text='Save', width = 20, command= lambda:save_new_product(product_dict, product_id_entry.get(),product_name_entry.get(), product_qtd_entry.get()))
    btn_save_prod.grid(row=4, column=2, sticky=tk.W, padx=5, pady=5)

    
    root.eval(f'tk::PlaceWindow {str(insert_product_window)} center')


def insert_product_clear():
    #Cleaning product id entry
    product_id_entry.delete(0,tk.END)
    #Cleaning product name entry
    product_name_entry.delete(0,tk.END)
    #Cleaning product Price entry
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
    product_id_entry.bind('<KeyRelease>', lambda  p=product_dict :alt_autocomplete(product_dict))

    lb2 = ttk.Label(alt_product_window, text="Product name:")
    lb2.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)

    global product_name_entry
    product_name_entry = ttk.Entry(alt_product_window, width = 50)
    product_name_entry.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5, columnspan=5)

    lb3 = ttk.Label(alt_product_window, text="Price:")
    lb3.grid(row=2, column=0, sticky=tk.E, padx=5, pady=5)

    global product_qtd_entry
    product_qtd_entry = ttk.Entry(alt_product_window, width = 20)
    product_qtd_entry.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
    
    btn_close_prod = ttk.Button(alt_product_window, text='Close', width = 20, command = lambda:exit(alt_product_window, product_dict))
    btn_close_prod.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)

    btn_save_prod = ttk.Button(alt_product_window, text='Save', width = 20, command= lambda:save_alt_product(product_dict, product_id_entry.get(),product_name_entry.get(), product_qtd_entry.get()))
    btn_save_prod.grid(row=4, column=2, sticky=tk.W, padx=5, pady=5)

    
    root.eval(f'tk::PlaceWindow {str(alt_product_window)} center')
    

def del_product(crud_win,product_dict):
    crud_win.destroy()
    # Creating delete product window
    del_product_window = tk.Toplevel(root)
    del_product_window.title('Pegasus - Product list management')
 
    lb1 = ttk.Label(del_product_window, text='Product ID:')
    lb1.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)

    global del_product_id_entry
    del_product_id_entry = ttk.Entry(del_product_window, width = 20)
    del_product_id_entry.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
    del_product_id_entry.bind('<KeyRelease>', lambda  p=product_dict :del_autocomplete(product_dict))

    lb2 = ttk.Label(del_product_window, text='Product name:')
    lb2.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)

    global del_product_name_entry
    del_product_name_entry = ttk.Label(del_product_window, text='')
    del_product_name_entry.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5, columnspan=5)

    lb3 = ttk.Label(del_product_window, text='Price:')
    lb3.grid(row=2, column=0, sticky=tk.E, padx=5, pady=5)

    global del_product_qtd_entry
    del_product_qtd_entry = ttk.Label(del_product_window, text='')
    del_product_qtd_entry.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

    
    
    btn_close_prod = ttk.Button(del_product_window, text='Close', width = 20, command = lambda:exit(del_product_window, product_dict))
    btn_close_prod.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)

    btn_delete_prod = ttk.Button(del_product_window, text='Delete', width = 20, command= lambda:exec_del_product(product_dict, del_product_id_entry.get()))
    btn_delete_prod.grid(row=4, column=2, sticky=tk.W, padx=5, pady=5)

    
    root.eval(f'tk::PlaceWindow {str(del_product_window)} center')


def alt_autocomplete(product_dict):  
    i = product_id_entry.get()
    if i in product_dict:
        #Product found
        l = product_dict[i] 
        #Cleaning entry fields
        product_name_entry.delete(0, tk.END)
        product_qtd_entry.delete(0, tk.END)
        #Showing product in the screen
        product_name_entry.insert(0, l[1])
        product_qtd_entry.insert(0, l[2])
    else:
        #Product not found
        #Cleaning protuct in screen
        product_name_entry.delete(0, tk.END)
        product_qtd_entry.delete(0, tk.END)

def del_autocomplete(product_dict):  
    i = del_product_id_entry.get()
    if i in product_dict:
        #Product found
        l = product_dict[i] 
        #Showing product in the screen
        del_product_name_entry.config(text = l[1])
        del_product_qtd_entry.config(text =l[2])
    else:
        #Product not found
        #Cleaning protuct in screen
        del_product_name_entry.config(text = '')
        del_product_qtd_entry.config(text = '')
        

def req_autocomplete(product_dict):  
    i = req_product_id.get()
    if i in product_dict:
        #Product found
        l = product_dict[i] 
        #Showing product in the screen
        req_product_name.config(text = l[1])
        req_product_price.config(text =l[2])
        req_product_qtd_entry.delete(0, tk.END)
    else:
        #Product not found
        #Cleaning protuct in screen
        req_product_name.config(text = '')
        req_product_price.config(text = '')
        req_product_qtd_entry.delete(0, tk.END)

def exit(win, product_dict):
    #Destroy current window
    win.destroy()
    #Show product list and crud window
    show_product_list(product_dict)

def messagebox_manager(code, msg, control):
    # code = 0 means product already exists
    answer = False
    if code == 0:
        messagebox.showwarning('Pegasus', msg)
    elif code == 1:
    # code = 1 means product saved/erased with success
        messagebox.showinfo('Pegasus', msg)
    elif code == 2:
    # code = 2 means error
        messagebox.showerror('Pegasus', msg)
    elif code == 3:
    # code = 3 means delete message
        answer = messagebox.askyesno(msg, 'Confirm action?')
    # After message return focus to product_id_entry
    elif code == 4:
    #Code 4 means operation canceled
        messagebox.showinfo('Pegasus', msg)
    elif code == 5:
    # Code 5 means product not find in request list
        messagebox.showwarning('Pegasus', msg)  

    control.focus()
    
    return answer



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
def save_dictionary_in_file(filename,dict, header):
    with open(filename, "w") as csv_file:
        #Save first line
        csv_file.write(header)
        for i in dict:
            l = dict[i]
            csv_file.write(f'{l[0]},{l[1]},{l[2]}\n')

def save_new_product(product_dict, id,name,qtd):
    """
        This function receives data from the product 
        being added to the list, checks if it exists, 
        and if it does not, saves it to the file.
    """
    try:
        if id in product_dict:
            code = 0
            msg = f'Product ID {id} already exists'
        else:
            Price = float(qtd)
            #creating a product list structure
            l = [id,name,qtd]
            #Store the new product in list
            product_dict[id] = l
            #Save new product in file
            file = path + filename
            header = 'Product #,Name,Price\n'
            #The function save_dictionary_in_file(file,product_dict, header),
            #saves the new item in the file that contains the list of stock products.
            save_dictionary_in_file(file,product_dict, header)
            code = 1
            msg = 'Data saved successfully'
            #The following function clears the product inclusion screen.
            insert_product_clear()
    except ValueError as val_err:
        code = 2
        msg = f'Invalid Price: {qtd}'
    except FileNotFoundError as file_err:
        code = 2
        msg = f'File {file} not found'
    finally:
        #The messagebox function is a hub
        #for showing dialog boxes to the user.
        if __name__ == "__main__":
            #If the function is called by the test module, then it does not execute the dialog box.
            messagebox_manager(code,msg, product_id_entry)
        return product_dict
        
def save_alt_product(product_dict, id,name,qtd):
    #The following function is used to save 
    #changes to items in the product list to a file.
    try:
        if id in product_dict:
            Price = float(qtd)
            #creating a product list structure
            l = [id,name,qtd]
            #Store the product in list
            product_dict[id] = l
             #Save new product in file
            file = path + filename
            header = 'Product #,Name,Price\n'
            #The function save_dictionary_in_file(file,product_dict, header),
            #saves the new item in the file that contains the list of stock products.
            save_dictionary_in_file(file,product_dict, header)
            code = 1
            msg = 'Data saved successfully'
        else:
            code = 0
            msg = f"Product ID {id} doesn't exists"
    
    except ValueError as val_err:
        code = 2
        msg = f'Invalid Price: {qtd}'
    except FileNotFoundError as file_err:
        code = 2
        msg = f'File {file} not found'
    finally:
        #The messagebox function is a hub
        #for showing dialog boxes to the user.
        if __name__ == "__main__":
            messagebox_manager(code,msg, product_id_entry)
        return product_dict

def exec_del_product(product_dict, id):
    #The following function is used to 
    #delete items from the product list
    #and save the new updated list to a file.
    try:  
        code = -1
        if id in product_dict:
            answer = messagebox_manager(3, f'Confirms deletion of the product with ID {id}', del_product_id_entry)
            if answer:
                product_dict.pop(id)
                file = path + filename
                header = 'Product #,Name,Price\n'
                #The function save_dictionary_in_file(file,product_dict, header),
                #saves the new item in the file that contains the list of stock products.
                save_dictionary_in_file(file,product_dict, header)
                code = 1
                msg = 'Data erased successfully'
            else:
                code = 4
                msg = 'Operation canceled'
                
        else:
            code = 0
            msg = f"Product ID {id} doesn't exists"
    except FileNotFoundError as file_err:
        code = 2
        msg = f'File {file} not found'
    finally:
        #The messagebox function is a hub
        #for showing dialog boxes to the user.
        messagebox_manager(code,msg, del_product_id_entry)
        return code
    


#Functions section end----------------------------------------------------------- 

#Product Management Section End -------------------------------------------------

"""
    The following section contains the creation and use of the request
    management module graphical interface and the associated supporting
    functions.

"""
#Request management section beguin-----------------------------------------------
#Creating request GUI
def request_window(product_dict):

    request_list = [['Id', 'Name', 'Price','Quantity', 'Total']]
    #creating request crud window
    req_win = tk.Toplevel(root)
    req_win.title('Pegasus - Request management')
   
    #Creating and organizing frames
    req_frame1 = Frame(req_win)
    req_frame1.grid(row=0, column=0, pady=5, padx=10, sticky=tk.W)
    
    req_frame2 = Frame(req_win)
    req_frame2.grid(row=1, column=0, pady=5, padx=10)

    global req_frame3
    req_frame3 = Frame(req_win)
    req_frame3.grid(row=2, column=0, pady=5, padx=10)

    #Creating and puting components on frames
    req_lb1 = ttk.Label(req_frame1, text='Product ID:')
    req_lb1.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)

    global req_product_id
    req_product_id = ttk.Entry(req_frame1, width = 30)
    req_product_id.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5, columnspan=3)
    req_product_id.bind('<KeyRelease>', lambda  p=product_dict :req_autocomplete(product_dict))

    req_lb2 = ttk.Label(req_frame1, text='Product name:')
    req_lb2.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)

    global req_product_name
    req_product_name = ttk.Label(req_frame1, text='')
    req_product_name.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5, columnspan=5)

    req_lb3 = ttk.Label(req_frame1, text='Price:')
    req_lb3.grid(row=2, column=0, sticky=tk.E, padx=5, pady=5)

    global req_product_price
    req_product_price = ttk.Label(req_frame1, width = 50,  text='')
    req_product_price.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5, columnspan=3)

    
    req_lb4 = ttk.Label(req_frame1, text='Quantity:')
    req_lb4.grid(row=3, column=0, sticky=tk.E, padx=5, pady=5)
    
    global req_product_qtd_entry
    req_product_qtd_entry = ttk.Entry(req_frame1, width = 25)
    req_product_qtd_entry.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5, columnspan=3)

    req_btn_close = ttk.Button(req_frame2, text='Close', width = 25, command= lambda:crud_win_exit(req_win))
    req_btn_close.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
    
    req_btn_insert = ttk.Button(req_frame2, text='Insert', width = 25, 
                                command= lambda:insert_request_item(product_dict, request_list, req_product_id.get(), req_product_name.cget("text"),
                                                                    req_product_price.cget("text"), req_product_qtd_entry.get()))
    req_btn_insert.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)

    req_btn_delete = ttk.Button(req_frame2, text='Delete', width = 25, command= lambda:delete_request_item(request_list, req_product_id.get()))
    req_btn_delete.grid(row=4, column=2, sticky=tk.W, padx=5, pady=5)

    req_btn_save = ttk.Button(req_frame2, text='Save', width = 25, command= lambda:save_request_item(request_list))
    req_btn_save.grid(row=4, column=3, sticky=tk.W, padx=5, pady=5)

    #Centralizing the window
    root.eval(f'tk::PlaceWindow {str(req_win)} center')   

#Functions

def insert_request_item(product_dict, request_list, req_id, req_product_name, req_product_price, req_product_qtd):
    
    #Creating and populating product list table
    #This screen show the product list
    class Table:
        def __init__(self,root, total_rows, total_columns):
             
            # code for creating table
            for i in range(total_rows):
                l = i % 2
                if l == 0:
                    color = 'white'
                else:
                    color = 'aliceblue'
                for j in range(total_columns):
                    if i == 0:
                        if j == 0 or j == 2:
                            self.e = Label(root, width=5, fg='blue', bg= 'wheat',
                                    font=('Arial',12,'bold'), borderwidth=2, relief="groove", text=request_list[i][j])
                        elif j ==1:
                            self.e = Label(root, width=35, fg='blue', bg= 'wheat',
                                    font=('Arial',12,'bold'), borderwidth=2, relief="groove", text=request_list[i][j])   
                        elif j == 3:
                            self.e = Label(root, width=10, fg='blue', bg= 'wheat',
                                    font=('Arial',12,'bold'), borderwidth=2, relief="groove", text=request_list[i][j]) 
                        elif j == 4:
                            self.e = Label(root, width=10, fg='blue', bg= 'wheat',
                                    font=('Arial',12,'bold'), borderwidth=2, relief="groove", text=request_list[i][j]) 
                        
                    else:
                        if j == 0 or j == 2:
                            self.e = Label(root, width=5, fg='black', bg=color,
                                    font=('Arial',10,'bold'), borderwidth=2, relief="groove", text=request_list[i][j])
                        elif j ==1:
                            self.e = Label(root, width=35, fg='black', bg=color,
                                    font=('Arial',10,'bold'), borderwidth=2, relief="groove", text=request_list[i][j])   
                        elif j == 3:
                            self.e = Label(root, width=10, fg='black',bg=color,
                                    font=('Arial',10,'bold'), borderwidth=2, relief="groove", text=request_list[i][j])
                        elif j == 4:
                            self.e = Label(root, width=10, fg='black', bg=color,
                                    font=('Arial',10,'bold'), borderwidth=2, relief="groove", text=request_list[i][j])
                    self.e.grid(row=i, column=j,sticky="nsew")

    # Testing if product exists in product list
    if req_id in product_dict:
        if req_product_qtd.isdigit():
            request_list.append([req_id, req_product_name, req_product_price, 
                            req_product_qtd, f'{(float(req_product_price) * float(req_product_qtd)):.2f}'])
            # initializing table
            # find total number of rows and
            # columns in list
            total_rows = len(request_list)
            total_columns = len(request_list[0])

            t = Table(req_frame3, total_rows, total_columns)
        else:
            code = 1
            msg = 'Invalid quantity value'
            messagebox_manager(code, msg, req_product_qtd_entry)
    else:
        code = 1
        msg = 'Invalid product'
        messagebox_manager(code, msg, req_product_id)

def delete_request_item(request_list, id):
    
    #Creating and populating product list table
    #This screen show the product list
    class Table:
        def __init__(self,root, total_rows, total_columns):
             
            # code for creating table
            for i in range(total_rows):
                l = i % 2
                if l == 0:
                    color = 'white'
                else:
                    color = 'aliceblue'
                for j in range(total_columns):
                    if i == 0:
                        if j == 0 or j == 2:
                            self.e = Label(root, width=5, fg='blue', bg= 'wheat',
                                    font=('Arial',12,'bold'), borderwidth=2, relief="groove", text=request_list[i][j])
                        elif j ==1:
                            self.e = Label(root, width=35, fg='blue', bg= 'wheat',
                                    font=('Arial',12,'bold'), borderwidth=2, relief="groove", text=request_list[i][j])   
                        elif j == 3:
                            self.e = Label(root, width=10, fg='blue', bg= 'wheat',
                                    font=('Arial',12,'bold'), borderwidth=2, relief="groove", text=request_list[i][j]) 
                        elif j == 4:
                            self.e = Label(root, width=10, fg='blue', bg= 'wheat',
                                    font=('Arial',12,'bold'), borderwidth=2, relief="groove", text=request_list[i][j]) 
                        
                    else:
                        if j == 0 or j == 2:
                            self.e = Label(root, width=5, fg='black', bg=color,
                                    font=('Arial',10,'bold'), borderwidth=2, relief="groove", text=request_list[i][j])
                        elif j ==1:
                            self.e = Label(root, width=35, fg='black', bg=color,
                                    font=('Arial',10,'bold'), borderwidth=2, relief="groove", text=request_list[i][j])   
                        elif j == 3:
                            self.e = Label(root, width=10, fg='black',bg=color,
                                    font=('Arial',10,'bold'), borderwidth=2, relief="groove", text=request_list[i][j])
                        elif j == 4:
                            self.e = Label(root, width=10, fg='black', bg=color,
                                    font=('Arial',10,'bold'), borderwidth=2, relief="groove", text=request_list[i][j])
                    self.e.grid(row=i, column=j,sticky="nsew")

    #Deleting item and constructing a new table on screen
    total_rows = len(request_list)
    k = 0
    for j in request_list:
        try:
            k += 1
            i = j.index(id)
            del request_list[k-1]
            code = 1
            msg =f'Product {id} deleted successfully .'
            total_rows = len(request_list)
            total_columns = len(request_list[0])
            if __name__ == "__main__":
                #Cleaning the grid, so we can rebuild it with the updated data.
                for widget in req_frame3.winfo_children():
                    widget.destroy() 
                t = Table(req_frame3, total_rows, total_columns)
        except ValueError as v_err:
            if k == total_rows: 
                code = 5
                msg = f'The product {id} is not in the order.'
    if __name__ == "__main__":
        messagebox_manager(code, msg, req_product_id)
    return request_list
            

def save_request_item(product_list):
        #The following functionality saves the order 
        #items to a file.
        try:
            code = 0
            filename = path + filename_request
            with open(filename, "w") as csv_file:
                for i in product_list:
                    csv_file.write(f'{i[0]},{i[3]}\n')   
                code = 1
                msg = f'Data saved successfully'
        except FileNotFoundError as file_err:
            code = 2
            msg = f'File {filename} not found'
        finally:
            if __name__ == "__main__":
                messagebox_manager(code, msg,req_product_qtd_entry)
            return code

# Call main to start this program.
if __name__ == "__main__":
    main()