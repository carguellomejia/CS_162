def rect_surface_area(length, width, height):
    # Creates functiom for the surface area of a rectangular solid.
    return 2 * rect_area(width * length) + 2 * (height * length) + 2 * (height * width)
    #  Returns formula for surface area  of a rectangular solid: 2*(w*l + h*l + h*w)


def main():
    length = int(input("Enter the length of the the object as in integer: "))
    # Asks for user input for the  value of length (l).
    width = int(input("Enter the width of the the object as in integer: "))
    # Asks for user input for the  value of width (w).
    height = int(input("Enter the height of the the object as in integer: "))
    # Asks for user input for the  value of height (h).
    total_area  = rect_surface_area(length, width, height)
    print("Length (l) = ", length, " Width (w) = ", width, "Height (h) = ", height)
    # Displays user input values pf l, w, and h.
    print("Total Surface Area = ", total_area)
    # Prints result of calculated surface area of a rectangular solid.
    # Made by Jerrod