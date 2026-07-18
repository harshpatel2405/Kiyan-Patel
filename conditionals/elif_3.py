'''
Input electricity units used and decide rate:
	0–100 units → ₹2/unit
	101–300 units → ₹3/unit
	301–500 units → ₹5/unit
	500 units → ₹8/unit
'''
units = int(input("Enter number of units consumed : "))
bill = 0
print("Units :", units)

if units > 0 and units <= 100:
    bill = units * 2
    print("Cost is 2 / unit")
elif units > 100 and units <= 300:
    bill = units * 3
    print("Cost is 3 / unit")
elif units > 300 and units <= 500:
    bill = units * 5
    print("Cost is 5 / unit")
elif units > 500:
    bill = units * 8
    print("Cost is 8 / unit")

print("Bill :", bill)
