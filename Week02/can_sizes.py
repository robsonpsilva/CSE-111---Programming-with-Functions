import math

def main():

    #Storage efficiency to Can #1 Picnic
    print(f'#1 Picnic {compute_storage_efficiency(6.83, 10.16):.2f}')

    #Storage efficiency to can # 1 Tall
    print(f'#1 Tall {compute_storage_efficiency(7.78, 11.91):.2f}')

    #Storage efficiency to can #2
    print(f'#2 {compute_storage_efficiency(8.73, 11.59):.2f}')

    #Storage efficiency to can #2.5
    print(f'#2.5 {compute_storage_efficiency(10.32, 11.91):.2f}')

    #Storage efficiency to can #3 cilinder
    print(f'#3 Cylinder {compute_storage_efficiency(10.79, 17.78):.2f}')

    #Storage efficiency to can #5
    print(f'#5 {compute_storage_efficiency(13.02, 14.29):.2f}')

    #Storage efficiency to can #6Z
    print(f'#6Z {compute_storage_efficiency(5.40, 8.89):.2f}')

    #Storage efficiency to can #8Z short
    print(f'#8Z short {compute_storage_efficiency(6.83, 7.62):.2f}')

    #Storage efficiency to can #10
    print(f'#10 {compute_storage_efficiency(15.72, 17.78):.2f}')

    #Storage efficiency to can #211
    print(f'#211 {compute_storage_efficiency(6.83, 12.38):.2f}')

    #Storage efficiency to can #300
    print(f'#300 {compute_storage_efficiency(7.62, 11.27):.2f}')

    #Storage efficiency to can #303
    print(f'#303 {compute_storage_efficiency(8.10, 11.11):.2f}')

    print('')
    print(10*'-')

    #Cost efficiency to Can #1 Picnic
    print(f'#1 Picnic {compute_cost_efficiency(6.83, 10.16, 0.28):.2f}')

    #Cost efficiency to can # 1 Tall
    print(f'#1 Tall {compute_cost_efficiency(7.78, 11.91, 0.43):.2f}')

    #Cost efficiency to can #2
    print(f'#2 {compute_cost_efficiency(8.73, 11.59, 0.45):.2f}')

    #Cost efficiency to can #2.5
    print(f'#2.5 {compute_cost_efficiency(10.32, 11.91, 0.61):.2f}')

    #Cost efficiency to can #3 cilinder
    print(f'#3 Cylinder {compute_cost_efficiency(10.79, 17.78, 0.86):.2f}')

    #Cost efficiency to can #5
    print(f'#5 {compute_cost_efficiency(13.02, 14.29, 0.83):.2f}')

    #Cost efficiency to can #6Z
    print(f'#6Z {compute_cost_efficiency(5.40, 8.89, 0.22):.2f}')

    #Cost efficiency to can #8Z short
    print(f'#8Z short {compute_cost_efficiency(6.83, 7.62, 0.26):.2f}')

    #Cost efficiency to can #10
    print(f'#10 {compute_cost_efficiency(15.72, 17.78, 1.53):.2f}')

    #Cost efficiency to can #211
    print(f'#211 {compute_cost_efficiency(6.83, 12.38, 0.34):.2f}')

    #Cost efficiency to can #300
    print(f'#300 {compute_cost_efficiency(7.62, 11.27, 0.38):.2f}')

    #Cost efficiency to can #303
    print(f'#303 {compute_cost_efficiency(8.10, 11.11, 0.42):.2f}')

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