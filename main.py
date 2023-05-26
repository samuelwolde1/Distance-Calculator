# Distance Calculator by Samuel Wolde

print("WELCOME TO THE DISTANCE CALCULATOR!")

# Recieve the coordinates from user
x1 = float(input("\nEnter x1 value: "))
y1 = float(input("Enter y1 value: "))
x2 = float(input("Enter x2 value: "))
y2 = float(input("Enter y2 value: "))

# Process the distance between points
distance = (((x2 - x1) **2 + (y2 - y1)) ** 1/2)
distance_rounded = round(distance, 2)

# Output the distance between the two points
print("\nDistance between the two points is " + str(distance_rounded))