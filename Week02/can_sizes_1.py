import math

def main():

    can_data = [['#1 Picnic', 6.83, 10.16, 0.28], ['#1 Tall', 7.78, 11.91, 0.43],
                ['#2', 8.73, 11.59, 0.45], ['#2.5', 10.32, 11.91, 0.61],
                ['#3 Cylinder', 10.79, 17.78, 0.86], ['#5', 13.02, 14.29, 0.83],
                ['#6Z', 5.40, 8.89, 0.22], ['#8Z short', 6.83, 7.62, 0.26],
                ['#10', 15.72, 17.78, 1.53], ['#211', 6.83, 12.38, 0.34],
                ['#300', 7.62, 11.27, 0.38], ['#303', 8.10, 11.11, 0.42]]
    
    #printing the storage eficiency
    print(20 * '_')
    print('')
    print('Storage efficiency')
    print(20 * '_')
    print('')

    for i in can_data:
        print(f'{i[0]} {compute_storage_efficiency(i[1], i[2]):.2f}')

    #printing the cost eficiency
    print(20 * '_')
    print('')
    print('Cost efficiency')
    print(20 * '_')
    print('')
   
    for j in can_data:
        print(f'{j[0]} {compute_cost_efficiency(j[1], j[2], j[3]):.2f}')

    print('')
    
def compute_cost_efficiency(radius, height, cost):
    volume = compute_volume(radius, height)
    efficiency = volume/cost
    return efficiency

def compute_volume(radius, height):
    """
    This function computes the volume of a cone
    They receive two variables, radius and height
    then compute the volume of a cone
    """
    volume = math.pi * (radius ** 2) * height
    return volume


def compute_surface_area(radius, height):
    """
    This function compute the surface of a cone
    They receive two variables, radius and height of the cone
    the compute the area of a cone
    """
    area = 2 * math.pi * radius * (radius + height)
    return area

def compute_storage_efficiency(radius, height):
    """
     This function calculates can's storage eficciency as a ratio between surface and area of a can

    """
    st_ef = compute_volume(radius,height) / compute_surface_area(radius,height)
    return st_ef

main()