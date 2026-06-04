i = int(input("Enter any Number: "))
count = 0

# Loop from 1 to i (inclusive)
for n in range(1, i + 1):
    if i % n == 0:
        count = count + 1
          # Prints the factor as it finds them

# The check must happen AFTER the loop finishes
if count == 2:
    print("Number is prime")
else:
    print("Number is not prime")
