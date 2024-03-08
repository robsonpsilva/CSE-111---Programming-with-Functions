import math

def main():
    #Storage efficiency to Can #1 Picnic
    print(f'#1 Picnic Can radius 6.83, height 10.16, Storage efficiency:  {storage_efficiency(6.83, 10.16)}')

    #Storage efficiency to can # 1 Tall
    print(f'#1 Tall Can radius 7.78, height 11.91, Storage efficiency:  {storage_efficiency(7.78, 11.91)}')

    #Storage efficiency to can #2
    print(f'#2  radius 8.73, height 11.59, Storage efficiency:  {storage_efficiency(8.73, 11.59)}')

    #Storage efficiency to can #2.5
    print(f'#2.5  radius 10.32, height 11.91, Storage efficiency:  {storage_efficiency(10.32, 11.91)}')

    #Storage efficiency to can #3 cilinder
    print(f'#3 cilinder  radius 10.79, height 17.78, Storage efficiency:  {storage_efficiency(10.79, 17.78)}')

    #Storage efficiency to can #5
    print(f'#5 radius 13.02, height 14.29, Storage efficiency:  {storage_efficiency(13.02, 14.29)}')

    #Storage efficiency to can #6Z
    print(f'#6Z radius 5.40, height 8.89, Storage efficiency: {storage_efficiency(5.40, 8.89)}')

    #Storage efficiency to can #8Z short
    print(f'#8Z short radius 6.83, height 7.62, Storage efficiency:  {storage_efficiency(6.83, 7.62)}')

    #Storage efficiency to can #10
    print(f'#10 radius 15.72, height 17.78, Storage efficiency:  {storage_efficiency(15.72, 17.78)}')

    #Storage efficiency to can #211
    print(f'#211 radius 6.83, height 12.38, Storage efficiency:  {storage_efficiency(6.83, 12.38)}')

    #Storage efficiency to can #300
    print(f'#300 radius 7.62, height 11.27, Storage efficiency:  {storage_efficiency(7.62, 11.27)}')

    #Storage efficiency to can #303
    print(f'#303 radius 8.10, height 11.11, Storage efficiency:  {storage_efficiency(8.10, 11.11)}')

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

def storage_efficiency(radius, height):
    """
     This function calculates can's storage eficciency as a ratio between surface and area of a can

    """
    st_ef = compute_volume(radius,height) / compute_surface_area(radius,height)
    return st_ef

main()