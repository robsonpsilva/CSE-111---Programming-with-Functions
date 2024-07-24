from sales import save_new_product, save_dictionary_in_file, save_alt_product
from sales import save_request_item, delete_request_item, read_dictionary_from_file
import csv #We use this library to be able to import and manipulate CSV files.
import pytest


def test_save_new_product():
    key_column_index = 0
    filename = 'products.csv'
    product_dict={'D150': ['D150', '1 gallon milk', '2.85'],
              'D083': ['D083', '1 cup yogurt', '0.75'], 
              'D215': ['D215', '1 lb cheddar cheese', '3.35']}
    id = 'W231'
    name = '32 oz granola'
    qtd = '3.21'
    dict = save_new_product(product_dict, id, name, qtd)
    assert dict['D150'] == ['D150', '1 gallon milk', '2.85']
    assert dict['D083'] == ['D083', '1 cup yogurt', '0.75']
    assert dict['D215'] == ['D215', '1 lb cheddar cheese', '3.35']
    assert dict['W231'] == ['W231','32 oz granola', '3.21' ]
    #Loading product list
    path = 'Final_Project/'
    file = path + filename
    products = read_dictionary_from_file(file, key_column_index)
    assert products['D150'] == ['D150', '1 gallon milk', '2.85']
    assert products['D083'] == ['D083', '1 cup yogurt', '0.75']
    assert products['D215'] == ['D215', '1 lb cheddar cheese', '3.35']
    assert products['W231'] == ['W231','32 oz granola', '3.21' ]

def test_save_dictionary_in_file():
    
    key_column_index = 0
    path = 'Final_Project/'
    filename = 'products.csv'
    file = path + filename
    header = 'Product #,Name,Price\n'
    dict={'D150': ['D150', '1 gallon milk', '2.85'],
              'D083': ['D083', '1 cup yogurt', '0.75'], 
              'D215': ['D215', '1 lb cheddar cheese', '3.35'],
              'W231': ['W231','32 oz granola', '3.21' ]}
    
    save_dictionary_in_file(file,dict, header)
    
    products = read_dictionary_from_file(file, key_column_index)
    assert products['D150'] == ['D150', '1 gallon milk', '2.85']
    assert products['D083'] == ['D083', '1 cup yogurt', '0.75']
    assert products['D215'] == ['D215', '1 lb cheddar cheese', '3.35']
    assert products['W231'] == ['W231','32 oz granola', '3.21' ]

def test_save_alt_product():

    product_dict={'D150': ['D150', '1 gallon milk', '2.85'],
              'D083': ['D083', '1 cup yogurt', '0.75'], 
              'D215': ['D215', '1 lb cheddar cheese', '3.35'],
              'W231': ['W231','32 oz granola', '3.21' ]}
    id = 'W231'
    name = '32 oz granola'
    qtd = '3.33'

    dict = save_alt_product(product_dict, id,name,qtd)

    assert dict['D150'] == ['D150', '1 gallon milk', '2.85']
    assert dict['D083'] == ['D083', '1 cup yogurt', '0.75']
    assert dict['D215'] == ['D215', '1 lb cheddar cheese', '3.35']
    assert dict['W231'] == ['W231','32 oz granola', '3.33' ]

    id = 'D150'
    name = 'twix candy bar'
    qtd = '0.85'

    dict = save_alt_product(product_dict, id,name,qtd)

    assert dict['D150'] == ['D150', 'twix candy bar', '0.85']
    assert dict['D083'] == ['D083', '1 cup yogurt', '0.75']
    assert dict['D215'] == ['D215', '1 lb cheddar cheese', '3.35']
    assert dict['W231'] == ['W231','32 oz granola', '3.33' ]

def test_save_request_item():
    
    filename_request = 'request.csv'
    path = 'Final_Project/'
    aux_list = []
    saved_list = []
    request_list = [['Id', 'Name', 'Price', 'Quantity', 'Total'], 
                    ['D150', '1 gallon milk', '2.85', '2', '5.70'], 
                    ['D083', '1 cup yogurt', '0.75', '3', '2.25'], 
                    ['D215', '1 lb cheddar cheese', '3.35', '4', '13.40']]
    
    assert save_request_item(request_list) == 1

    filename = path + filename_request
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:
            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:
                # From the current row, retrieve the data
                # from the column that contains the key.
                aux_list.append(row_list)

    saved_list = [['D150','2'],
                  ['D083','3'],
                  ['D215','4']]
    assert saved_list == aux_list
    



def test_delete_request_item():
    request_list = [['Id', 'Name', 'Price', 'Quantity', 'Total'], 
                    ['D150', '1 gallon milk', '2.85', '2', '5.70'], 
                    ['D083', '1 cup yogurt', '0.75', '3', '2.25'], 
                    ['D215', '1 lb cheddar cheese', '3.35', '4', '13.40']]
    test_list = [['Id', 'Name', 'Price', 'Quantity', 'Total'], 
                    ['D150', '1 gallon milk', '2.85', '2', '5.70'],
                    ['D215', '1 lb cheddar cheese', '3.35', '4', '13.40']]
    result_list = delete_request_item(request_list, 'D083')

    #First assert call
    assert result_list == test_list

    request_list = [['Id', 'Name', 'Price', 'Quantity', 'Total'], 
                    ['D150', '1 gallon milk', '2.85', '2', '5.70'], 
                    ['D083', '1 cup yogurt', '0.75', '3', '2.25'], 
                    ['D215', '1 lb cheddar cheese', '3.35', '4', '13.40'],
                    ['W231','32 oz granola', '3.33' ]]
    test_list = [['Id', 'Name', 'Price', 'Quantity', 'Total'], 
                    ['D150', '1 gallon milk', '2.85', '2', '5.70'], 
                    ['D083', '1 cup yogurt', '0.75', '3', '2.25'], 
                    ['D215', '1 lb cheddar cheese', '3.35', '4', '13.40']]
    result_list = delete_request_item(request_list, 'W231')

    assert result_list == test_list


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])