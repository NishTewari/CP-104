"""
------------------------------------------------------------------------
Write and test a program that prompts the user to enter:

the diameter of the base (cm)
the height of the cylinder (cm)
the cost of the material ($ per square cm)
number of containers to produce

Calculate the surface area of the container
------------------------------------------------------------------------
Author: Nish Tewari 
ID:     190684430
Email:  tewa4430@mylaurier.ca 
__updated__ = "2021-02-16"
------------------------------------------------------------------------
"""
#Constants
MATH_PI = 3.14

#user input variables 
diameter_container = float(input("Diamter of container base (cm): "))
height_container = float(input("Height of container (cm): "))
cost_material = float(input("Cost of material ($/cm^2): "))
num_of_containers = int(input("Number of containers: "))

#calculating radius 
radius_container = diameter_container / 2

#calculating surface area
surface_area_container = 2*MATH_PI*radius_container*height_container + ((radius_container**2) *MATH_PI)

#finding the cost of one container 
container_cost = surface_area_container * cost_material

#finding the cost of the all the containers
total_cost = container_cost * num_of_containers

print("The cost of one container is: ${:.2f}".format(container_cost))
print("The total cost of all containers is ${:.2f}".format(total_cost))