"""
Work as a team to write a Python program named discount.py that gets a customer’s 
subtotal as input and gets the current day of the week from your computer’s operating system. 
Your program must not ask the user to enter the day of the week. Instead, it must get the day 
of the week from your computer’s operating system.

If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program must 
subtract 10% from the subtotal. Your program must then compute the total amount due by 
adding sales tax of 6% to the subtotal. Your program must print the discount amount if 
applicable, the sales tax amount, and the total amount due.

Core Requirements
Your program asks the user for the subtotal but does not ask the user for the day of the week. 
Your program gets the day of the week from your computer’s operating system.
Your program correctly computes and prints the discount amount if applicable.
Your program correctly computes and prints the sales tax amount and the total amount due.
"""
from datetime import datetime

try:
    sub_total = float(input('Please enter the subtotal: '))
    current_date_and_time = datetime.now()
    day_of_week = current_date_and_time.weekday()
    total = 0
    discount = 0
    if sub_total >= 50: #Verify if subtotal is greater than 50, a condition to get discount
        if day_of_week in (1,2): # Verify if today is tuesday or wednesday, another condition to discount
            discount = 0.1 * sub_total
            print(f'Discount amount: {discount:.2f}')
            sub_total = sub_total - discount #Apply discount
            sales_tax_amount = sub_total * 0.06 #Calculate the tax_amount
            total = sub_total + sales_tax_amount
        else:
            sales_tax_amount = sub_total * 0.06 #Calculate the tax_amount
            total = sub_total + sales_tax_amount
    else:
        sales_tax_amount = sub_total * 0.06 #Calculate the tax_amount
        total = sub_total + sales_tax_amount
    
    print(f'Sales tax amount: {sales_tax_amount:.2f}')
    print(f'Total: {total:.2f}')
except ValueError:
    print('Attention: Data entry is not a number!')