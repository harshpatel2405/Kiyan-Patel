# reverse the number
n = 1234
rev = 0

while n > 0:
    ld = n % 10
    rev = rev * 10 + ld
    n = n // 10

print("reverse :", rev)


# 0 * 10 + 4 = 4 = rev
# 4 * 10 + 3 = 43
# 43 * 10 + 2 = 432
# 432 * 10 + 1 = 4321 = rev

n = 101
temp = n
rev = 0

while n > 0:
    ld = n % 10
    rev = rev * 10 + ld
    n = n // 10  # decrement (value of n becomes zero)

# original and reverse are same or not
if rev == temp:
    print(temp, "is palindrome number")
else:
    print(temp, "is not palindrome number")
