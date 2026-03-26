name = input("Enter driver name: ")
distance = float(input("Enter distance (km): "))
fuel_consumption = float(input("Enter fuel consumption (L/100km): "))
fuel_price = float(input("Enter fuel price (KZT/L): "))

litres_needed = distance * fuel_consumption / 100
fuel_cost = litres_needed * fuel_price
cost_per_km = fuel_cost / distance

print(
    f"""
{'='*30}
ROAD TRIP SUMMARY
{'='*30}
Driver : {name}
Distance : {distance} km
Consumption : {fuel_consumption} L/100km
Fuel price : {fuel_price} KZT/L
{'-'*30}
Litres needed: {litres_needed} L
Fuel cost : {fuel_cost} KZT
Cost per km : {cost_per_km} KZT
{'='*30}
"""
)
comparison1 = bool(distance >= 300)
comparison2 = bool(fuel_cost >= 5000)
print("Trip longer than 300 km: ", comparison1)
print("Fuel cost above 5000 KZT: ", comparison2)