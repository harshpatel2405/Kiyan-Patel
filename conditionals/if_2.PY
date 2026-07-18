# * check whether the number is divisible by 3 and 5

a = int(input("Enter a number : "))

if a % 3 == 0 and a % 5 == 0:
    print("Number is divisible by 3 and 5")
else:
    print("Number is not divisible by 3 and 5")

#  * check whether the number is divisible by 3 or 5
# * check whether the number is divisible by 3 and 5 

a = 15
b = 95
c = 89

sum = a + b + c
if(sum > 250):
    print("Grade A")
elif sum < 250 and sum > 150:
    print("Grade B")
else:
    print("Fail")