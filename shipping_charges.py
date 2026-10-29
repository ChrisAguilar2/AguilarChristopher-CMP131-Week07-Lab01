kgw = float(input("Enter the package weight in kilograms: "))
while kgw <= 0 or kgw > 20:
    print("Invalid weight please try again")
    kgw = float(input("Try again: "))
print("Valid number")
distance_m = float(input("Enter the shipping distance in miles:  "))
while distance_m < 10 or distance_m > 3000:
    print("Invalid distance please try again: ")
    distance_m = float(input("Try again: "))
print("Valid number")

if kgw <= 2:
    rate_kgw = 1.10
    shipping_charge = 1.10 * distance_m / 500
elif kgw > 2 and kgw <= 6:
    rate_kgw = 2.20
    shipping_charge = 2.20 * distance_m / 500
elif kgw > 6 and kgw <= 10:
    rate_kgw = 3.70
    shipping_charge = 3.70 * distance_m / 500
elif kgw > 10 and kgw <= 20:
    rate_kgw = 4.80
    shipping_charge = 4.80 * distance_m / 500

total = shipping_charge

print("=======================")
print("--Shipping Charges--")
print(f"Package Weight: {kgw:.2f}kg")
print(f"Shipping Distance: {distance_m:.2f}mi")
print(f"Rate per 500 miles : ${rate_kgw:.2f}")
print(f"Total shipping charge: ${total:.2f}") 
print("========================")