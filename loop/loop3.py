# * print and count digits
n = 1234
count = 0

while n > 0:
    ld = n % 10
    print(ld)
    count += 1
    n = n // 10

print("Number of Digits : ", count)

# * sum of digits
n = 1234
sum = 0

while n > 0:
    ld = n % 10
    sum = sum + ld
    n = n // 10

print("sum : ", sum)

# * multiplication of digits
n = 1234
mul = 1

while n > 0:
    ld = n % 10
    mul = mul * ld
    n = n // 10 
    
print("Multiplication : ", mul) 