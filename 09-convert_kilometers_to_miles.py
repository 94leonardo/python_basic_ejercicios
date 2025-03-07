# conversion fator

kilometers = float(input("Enter distance in kilometers: "))

# Convesion factor: 1 kilometer = 0.621371 miles
conversion_factor = 0.621371
miles = kilometers * conversion_factor

print(f"{kilometers} Kilometers is equal to {miles} miles.")
