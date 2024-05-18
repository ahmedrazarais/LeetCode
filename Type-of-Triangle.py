# You are given a 0-indexed integer array nums of size 3 which can form the sides of a triangle.

# A triangle is called equilateral if it has all sides of equal length.
# A triangle is called isosceles if it has exactly two sides of equal length.
# A triangle is called scalene if all its sides are of different lengths.
# Return a string representing the type of triangle that can be formed or "none" if it cannot form a triangle.

def triangleType(nums):
        # first checking there must be 3 inputs to check triangle saides condition
        if len(nums)<3:
            return False

        # variables to store sides
        # Unpacking the list elements into separate variables
        a, b, c = nums

            # Check the triangle inequality theorem
        if a + b > c and a + c > b and b + c > a:
            # Check for equilateral triangle
            if a == b and b == c:
                return "equilateral"
            # Check for isosceles triangle
            elif a == b or b == c or a == c:
                return "isosceles"
            # If not equilateral or isosceles, it must be scalene
            else:
                return "scalene"
        else:
            return "none"
        

print(triangleType([3,3,3]))