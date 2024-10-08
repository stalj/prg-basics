###
# The program calculates the cost of transporting goods
# based on the given distance in km, fuel price per 1 liter,
# and fuel consumption in liters per 100 km.
#
distance = float(input("Distance of transportation: "))
fuel_price = float(input("Fuel price per liter (in ZŁ): "))
fuel_consumption = float(input("Fuel consumption in liters per 100km: "))
transportation_cost = distance/100*fuel_consumption*fuel_price
print(f"Transportation cost: {round(transportation_cost, 2)} ZŁ")