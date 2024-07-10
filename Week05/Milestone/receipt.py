import csv

#Robson Paulo da Silva

key_column_index = 0
request_product_index = 0
request_quantity_index = 1
product_name_index = 1
product_price_index = 2

def main():
    products_dict = read_dictionary('Week05/Milestone/products.csv', key_column_index)
    print('All products')
    print(products_dict)
    
    print('Requested Items')
    """
   All Products
    {'D150': ['D150', '1 gallon milk', '2.85'], 'D083': ['D083',
    '1 cup yogurt', '0.75'], 'D215': ['D215', '1 lb cheddar
    cheese', '3.35'], 'P019': ['P019', 'iceberg lettuce',
    '1.15'], 'P020': ['P020', 'green leaf lettuce', '1.79'],
    'P021': ['P021', 'butterhead lettuce', '1.83'], 'P025':
    ['P025', '8 oz arugula', '2.19'], 'P143': ['P143', '1 lb
    baby carrots', '1.39'], 'W231': ['W231', '32 oz granola',
    '3.21'], 'W112': ['W112', 'wheat bread', '2.55'], 'C013':
    ['C013', 'twix candy bar', '0.85'], 'H001': ['H001', '8
    rolls toilet tissue', '6.45'], 'H014': ['H014', 'facial
    tissue', '2.49'], 'H020': ['H020', 'aluminum foil', '2.39'],
    'H021': ['H021', '12 oz dish soap', '3.19'], 'H025':
    ['H025', 'toilet cleaner', '4.50']}
    Requested Items
    wheat bread: 2 @ 2.55
    1 cup yogurt: 4 @ 0.75
    32 oz granola: 1 @ 3.21
    twix candy bar: 2 @ 0.85
    1 cup yogurt: 3 @ 0.75
    """
    list = read_list('Week05/Milestone/request.csv')
    for i in list:
        product_code = i[request_product_index]
        quantity = i[request_quantity_index]
        product = products_dict[product_code]
        product_name = product[product_name_index]
        product_price = product[product_price_index]
        print(f'{product_name}: {quantity} @ {product_price}')


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