"""
    Problem Statement
Many vehicle owners record the fuel efficiency of their vehicles as a way to track the health of the vehicle. If the fuel efficiency of a vehicle suddenly drops, there is probably something wrong with the engine or drive train of the vehicle. In the United States, fuel efficiency for gasoline powered vehicles is calculated as miles per gallon. In most other countries, fuel efficiency is calculated as liters per 100 kilometers.

The formula for computing fuel efficiency in miles per gallon is the following:

mpg =   (end − start)/gallons

where start and end are both odometer values in miles and gallons is a fuel amount in U.S. gallons.

The formula for converting miles per gallon to liters per 100 kilometers is the following:

lp100k =  235.215/mpg
"""
def main():
    try:
        start_odometer_value = int(input('Enter the first odometer reading (miles):'))
        end_odometer_value = int(input('Enter the second odometer reading (miles):'))
        amount_fuel_used = int(input('Enter the amount of fuel used (gallons):'))
        return True
    except ValueError:
        print('Attention: Data entry is not a number!')
        return False

def miles_per_gallon(start_value, end_value, amount_fuel_value):
    