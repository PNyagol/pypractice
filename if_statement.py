is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")


elif is_cold:
    print("It's a cold day")
    print("Wear warm cloths")

else:
    print("Enjoy your day")

# Test

price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price

else:
    down_payment = 0.2 * price

print(f"Down Payment = ${down_payment}")