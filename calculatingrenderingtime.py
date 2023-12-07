#Calculating time it takes to render with Evee and Cycle
import math

# Step 1: Get user input for camera coordinates
camera_x = float(input("Enter the x-coordinate of the camera: "))
camera_y = float(input("Enter the y-coordinate of the camera: "))

# Object is at the center (0, 0)
object_x, object_y = 0, 0

# Step 2: Calculate distance using Pythagorean theorem
distance = math.sqrt((camera_x - object_x)**2 + (camera_y - object_y)**2)

# Step 3: Print out the distance
print(f"The distance between the camera and the object is: {distance}")
