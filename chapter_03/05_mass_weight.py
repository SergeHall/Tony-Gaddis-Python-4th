# mass and weight.

mass = float(input("Please enter the mass the object's mass: "))
weight = mass * 9.8

print("Weight is", format(weight, ".2f"), "newtons.")
if weight > 500:
    print("It is too heavy!")
elif weight < 100:
    print("It is too light!")
