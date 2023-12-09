import math

# Step 1: Ask for the x and y values for the camera location
camera_x = float(input("Enter the x-coordinate of the camera: "))
camera_y = float(input("Enter the y-coordinate of the camera: "))

# Step 2: Calculate the distance using the Pythagorean theorem
object_x = 0  # Assuming the object is at the center (0, 0)
object_y = 0

distance = math.sqrt((camera_x - object_x)**2 + (camera_y - object_y)**2)

# Step 3: Print out the distance and how it was calculated
print(f"The distance between the camera and the object is {distance:.2f} meters.")
print(f"Calculation: sqrt(({camera_x} - {object_x})^2 + ({camera_y} - {object_y})^2)")
