"""
    Problem Statement
Many vehicle owners record the fuel efficiency of their vehicles as a way to track the health of the vehicle. If the fuel efficiency of a vehicle suddenly drops, there is probably something wrong with the engine or drive train of the vehicle. In the United States, fuel efficiency for gasoline powered vehicles is calculated as miles per gallon. In most other countries, fuel efficiency is calculated as liters per 100 kilometers.

The formula for computing fuel efficiency in miles per gallon is the following:

mpg =   (end − start)/gallons

where start and end are both odometer values in miles and gallons is a fuel amount in U.S. gallons.

The formula for converting miles per gallon to liters per 100 kilometers is the following:

lp100k =  235.215/mpg
"""
start_odometer_value = 0
end_odometer_value = 0
amount_fuel_used = 0

def main():
    # Get an odometer value in U.S. miles from the user.

    # Get another odometer value in U.S. miles from the user.

    # Get a fuel amount in U.S. gallons from the user.

    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.

    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.

    # Display the results for the user to see.
    try:
        start_odometer_value = int(input('Enter the first odometer reading (miles):'))
        end_odometer_value = int(input('Enter the second odometer reading (miles):'))
        amount_fuel_used = float(input('Enter the amount of fuel used (gallons):'))
        mpg = miles_per_gallon(start_odometer_value,end_odometer_value,amount_fuel_used)
        lp100k = lp100k_from_mpg(mpg)
        print(f'{mpg:.2f} miles per gallon')
        print(f'{lp100k:.2f} liters per 100 kilometers')
        return True
    except ValueError:
        print('Attention: Data entry is not a number!')
        return False

def miles_per_gallon(start_value = start_odometer_value, end_value = end_odometer_value, 
                     amount_fuel_value = amount_fuel_used):
   """
        Compute and return the average number of miles
        that a vehicle traveled per gallon of fuel.

        Parameters
            start_miles: An odometer value in miles.
            end_miles: Another odometer value in miles.
            amount_gallons: A fuel amount in U.S. gallons.
        Return: Fuel efficiency in miles per gallon.
    """
   mpg = (end_value - start_value) / amount_fuel_value
   return mpg
def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    lp_100k = 235.215 / mpg
    return lp_100k

main()