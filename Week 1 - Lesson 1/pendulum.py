"""
The time in seconds that a pendulum takes to swing back and
forth once is given by this formula:
             ____
            / h
    t = 2π / ----
          √  9.81

t is the time in seconds,
π is the constant PI, which is the ratio of the circumference
    of a circle divided by its diameter (use math.pi),
h is the length of the pendulum in meters.

Write a program that prompts a user to enter the length of a
pendulum in meters and then computes and prints the time in
seconds that it takes for that pendulum to swing back and forth.
"""
import math
try:
    length_of_pendulum = float(input('Length of pendulum (meters): '))
    t = 2 * math.pi * math.sqrt(length_of_pendulum / 9.81)
    print(f'Time (seconds):{t:.2f}')
except ValueError:
    print('Attention: Data entry is not a number!')