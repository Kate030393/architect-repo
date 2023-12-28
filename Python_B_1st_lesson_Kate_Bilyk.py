## First task
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
print(f"Sum: {a + b + c}")
print(f"Multiplying: {a * b * c}")

## Second task
diag_1 = int(input("Enter the length of the first diagonal: "))
diag_2 = int(input("Enter the length of the second diagonal: "))
s_romb = diag_1 * diag_2 / 2
print(f"Romb square: {s_romb}")

## Third task variant 1
a = int(input("Enter a four-digit number: "))
n1 = a // 1000
n2 = a // 100 % 10
n3 = a // 10 % 10
n4 = a % 10
result = n1 * n2 * n3 * n4
print(f"Digits multiplying: {result}")

## Third task variant 2
a = input("Enter a four-digit number: ")
result = int(a[0]) * int(a[1]) * int(a[2]) * int(a[3])
print(f"Digits multiplying: {result}")

## Third task variant 3
a = input("Enter a four-digit number: ")
result = 1
for i in range(len(a)):
    result *= int(a[i])
print(f"Digits multiplying: {result}")
