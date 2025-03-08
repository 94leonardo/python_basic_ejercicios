import math

# Input coefficientes

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
# calculate the discriminant

discriminant = b**2 - 4*a*c
# check if the  disciminante is positive ,  negative or zero

if discriminant > 0:
    # two real and distinct roots
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"The roots are: {root1}")
    print(f"The roots are: {root2}")
elif discriminant == 0:
    # One real root(repeated)
    root = -b / (2*a)
    print(f"Root: {root}")
else:
    # complex roots
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-discriminant) / (2*a)
    print(f"Roots: {real_part} + {imaginary_part}i")
    print(f"Roots: {real_part} - {imaginary_part}i")
