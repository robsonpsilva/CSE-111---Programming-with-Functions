from sales import save_new_product, save_dictionary_in_file, save_alt_product
from sales import save_request_item, delete_request_item, read_dictionary_from_file
import pytest




filename_request = 'request.csv'
path = 'Final_Project/'

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
    file = path + filename
    products = read_dictionary_from_file(file, key_column_index)
    assert products['D150'] == ['D150', '1 gallon milk', '2.85']
    assert products['D083'] == ['D083', '1 cup yogurt', '0.75']
    assert products['D215'] == ['D215', '1 lb cheddar cheese', '3.35']
    assert products['W231'] == ['W231','32 oz granola', '3.21' ]

def test_save_dictionary_in_file():
    
    key_column_index = 0
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

def test_save_request_item():
    save_request_item(product_list)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])