#Robson Paulo da Silva
import csv
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime


key_column_index = 0
request_product_index = 0
request_quantity_index = 1
product_name_index = 1
product_price_index = 2

store_name = 'Andarai Emporium'

def main():
    try:
        # Loading product list
        products_dict = read_dictionary('Week05/Prove/products.csv', key_column_index)
        #Loading client request
        list = read_list('Week05/Prove/request.csv')
        # Printing the store name
        print(15 * '-')
        print(store_name)
        print(15 * '-')
        # Printing ordered items'list
        total_items = 0
        subtotal = 0
        sales_tax = 0

        for i in list:
            product_code = i[request_product_index]
            quantity = i[request_quantity_index]
            product = products_dict[product_code]
            product_name = product[product_name_index]
            product_price = product[product_price_index]
            print(f'{product_name}: {quantity} @ {product_price}')
            total_items += float(quantity)
            subtotal += (float(product_price ) * float(quantity))
        
        # Printing total of items
        print(15 * '-')
        print(f'Number of items: {total_items:.1f}')

        #Printing subtotal
        print(f'Subtotal: {subtotal:.2f}')

        #Calculating sales tax
        sales_tax = subtotal * 0.06
        #Printing Sales Tax
        print(f'Sales Tax: {sales_tax:.2f}')

        #Printing total
        print(f'Total: {subtotal + sales_tax:.2f}')

        # Printing final message
        print('Thank you for shopping at the ' + store_name)

        
        # Call the now() method to get the current
        # date and time as a datetime object from
        # the computer's operating system.
        current_date_and_time = datetime.now()
        # Use an f-string to print the current
        # day of the week and the current time.
        print(f"{current_date_and_time:%a %b %d %I:%M:%S %Y}")

    #Handling exceptions
    except FileNotFoundError as not_found_err:
        print(not_found_err)
    except PermissionError as perm_err:
        print(perm_err)
    except ValueError as val_err:
        print(val_err)
    except KeyError as key_error:
        print(key_error)

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

def read_list(filename):
    """Read the contents of a CSV file into a compound
    list and return the list. Each element in the
    compound list will be a small list that contains
    the values from one row of the CSV file.
    Parameter filename: the name of the CSV file to read
    Return: a list of lists that contain strings
    """
    # Create an empty list that will
    # store the data from the CSV file.
    list = []
    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:
        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)
        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)
        for row_list in reader:
            # If the current row is not blank,
            # append it to the compound_list.
            if len(row_list) != 0:
                # Append one row from the CSV
                # file to the compound list.
                list.append(row_list)
    # Return the compound list.
    return list


# Call main to start this program.
if __name__ == "__main__":
    main()