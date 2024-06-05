import math
from datetime import datetime

"""
The size of a car tire in the United States is represented with three numbers like this: 205/60R15. The first number is the width of the tire in millimeters. The second number is the aspect ratio. The third number is the diameter in inches of the wheel that the tire fits. The volume of space inside a tire can be approximated with this formula:

v = 
π * w2* a(w*a + 2,540 * d)/10,000,000,000
v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.
"""
"""
    Exceeding requirements

    1- The system finds the price using the data entered by the user and prints it on the screen.
    2- If the user wants to buy the tire for which he entered the data, the system requests the telephone number.
    3- If the user enters non-numeric inputs for data whose inputs should be numeric, the system catches the error using a try->except structure.
"""

tyres_prices = [[185,65,15, 51.0],[205,60,15, 53.01],[175,70,14,39.12],[195,65,15,82.3], [185,50,14, 100.1]]

try:
    w = int(input('Enter the width of the tire in mm (ex 205): '))
    a =int(input('Enter the aspect ratio of the tire (ex 60): '))
    d = int(input('Enter the diameter of the wheel in inches (ex 15): '))

    v = math.pi * (w ** 2) * a * (w * a + 2540 * d) / 10000000000
    print(f'The approximate volume is {v:.2f} liters')
    
    #Exceeding requirements
    pricefound = False
    for t in tyres_prices:
        if t[0] == w and t[1] == a and t[2] == d:
            print(f'The tire price is {t[3]:.2f}')
            pricefound = True
            break
    if pricefound == False:
        print('Item not found in price list')

    #Opening file volumes.txr for appending text
    with open('volumes.txt', 'at') as volumes_file: 
        #Geting current system date
        current_date_and_time = datetime.now()
        #Recording the file
        #Exceeding requirements
        option = input('Do you want to buy the tires in the size you indicated?: Type 1 for Yes or anything else for No. ')
        if option.lower() == '1':
            #Exceeding requirements
            phone = input('Please type your phone number ')
            print(f'{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}, {phone}', file=volumes_file)
        else:
            print(f'{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}', file=volumes_file)
except ValueError:
    print('Attention: Data entry is not a number!')
