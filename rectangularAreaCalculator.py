def calculateRectangularArea(length, width):
    return {
        "imperial": length * width,
        "metric": (length * width) / 10.764
    }

print(calculateRectangularArea(int(input()), int(input())))