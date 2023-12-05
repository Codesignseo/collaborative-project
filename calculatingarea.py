# Getting the volume of different shapes
import math

def calculate_volume(shape):
    if shape.lower() == 'cube':
        length = float(input("Enter the length of the cube (in meters): "))
        volume = length**3
        work = f'V = length * length * length = {length} * {length} * {length} = {volume} m^3'
    elif shape.lower() == 'sphere':
        radius = float(input("Enter the radius of the sphere (in meters): "))
        volume = (4/3) * math.pi * radius**3
        work = f'V = (4/3) * π * radius^3 = (4/3) * π * {radius}^3 = {volume} m^3'
    elif shape.lower() == 'cylinder':
        radius = float(input("Enter the radius of the cylinder (in meters): "))
        height = float(input("Enter the height of the cylinder (in meters): "))
        volume = math.pi * radius**2 * height
        work = f'V = π * radius^2 * height = π * {radius}^2 * {height} = {volume} m^3'
    # Add more shapes as needed
    
    # Display the result
    result = f'The volume of the {shape} is {volume} m^3.'
    print(result)
    print(work)

# Get the shape from the user
shape = input("Enter the shape for which you want to calculate the volume: ")

# Calculate and display the volume
calculate_volume(shape)
