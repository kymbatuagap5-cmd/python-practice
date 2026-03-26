name = input("Enter driver name: ")
destination = input("Enter destination: ")
distance = float(input("Enter distance (km): "))
fuel_consumption = float(input("Enter fuel consumption (L/100km): "))
fuel_price = float(input("Enter fuel price (KZT/L): "))

litres_needed = distance * fuel_consumption / 100
fuel_cost = litres_needed * fuel_price
cost_per_km = fuel_cost / distance

if distance < 100:
    category = "Short trip"
elif 100 <= distance < 500:
    category = "Medium trip"
else:
    category = "Long trip"

print(f"""
{'='*30}
Driver : {name}
Destination : {destination.upper()}
Distance : {distance} km
Fuel cost : {fuel_cost} KZT
Category : {category}
{'='*30}
""")

destination_lower_case = destination.lower()
print("Destination uppercase : ", destination.upper())
print("Destination lowercase : ", destination_lower_case)
print("Length : ", len(destination))
print("Letter 'a' count", destination_lower_case.count("a"))