'''
Define a class Circle with instance object variable radius. Provide setter and getter for radius. Also define getArea() and getCircumference() methods. 
'''
class Circle:
    def __init__(self, radius=0):
        self._radius = radius  # Using a protected variable to store radius

    # Getter method for radius
    def get_radius(self):
        return self._radius

    # Setter method for radius
    def set_radius(self, radius):
        if radius >= 0:
            self._radius = radius
        else:
            raise ValueError("Radius cannot be negative")

    # Method to calculate the area of the circle
    def get_area(self):
        return 3.14159 * self._radius * self._radius

    # Method to calculate the circumference of the circle
    def get_circumference(self):
        return 2 * 3.14159 * self._radius

# Example usage
circle = Circle(5)
print(f"Radius: {circle.get_radius()}")
print(f"Area: {circle.get_area()}")
print(f"Circumference: {circle.get_circumference()}")

circle.set_radius(10)
print(f"New Radius: {circle.get_radius()}")
print(f"New Area: {circle.get_area()}")
print(f"New Circumference: {circle.get_circumference()}")


'''
An instance object variable radius.
Setter and getter methods for radius.
Methods to calculate the area and circumference of the circle.

Explanation:
Constructor __init__: Initializes the circle with a default radius of 0.
Getter get_radius: Returns the current radius.
Setter set_radius: Sets the radius to a new value if it is non-negative; otherwise, raises a ValueError.
Method get_area: Calculates and returns the area of the circle using the formula 
𝜋 × radius^2.

Method get_circumference: Calculates and returns the circumference of the circle using the formula 
2 × 𝜋 × radius.
This class encapsulates the radius property and provides methods to calculate the circle's area and circumference. You can modify the radius using the setter and retrieve the current radius using the getter.
'''