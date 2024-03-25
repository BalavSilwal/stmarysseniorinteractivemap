 import math

def check_triangle_properties(side1, side2, side3):
    is_equilateral = False
    is_isosceles = False
    is_scalene = False
    is_right = False

    if side1 == side2 and side2 == side3:
        is_equilateral = True
    elif side1 == side2 or side2 == side3 or side1 == side3:
        is_isosceles = True
    else:
        is_scalene = True

    if math.isclose(side1**2 + side2**2, side3**2) or math.isclose(side2**2 + side3**2, side1**2) or math.isclose(side1**2 + side3**2, side2**2):
        is_right = True

    return is_equilateral, is_isosceles, is_scalene, is_right
