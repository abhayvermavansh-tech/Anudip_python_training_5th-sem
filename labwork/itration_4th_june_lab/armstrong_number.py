# Armstrong Number Checker

num = int(input("Enter a number: "))

original_num = num
sum_of_cubes = 0

while num > 0:
    digit = num % 10
    sum_of_cubes += digit ** 3
    num //= 10

if sum_of_cubes == original_num:
    print(original_num, "is an Armstrong Number")
else:
    print(original_num, "is not an Armstrong Number")
