import math

def main():
    #Storage efficiency to Picnic
    print(f'1#{storage_efficiency(6.83, 10.16)}')

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
    st_ef = compute_volume / compute_surface_area
    return st_ef

main()