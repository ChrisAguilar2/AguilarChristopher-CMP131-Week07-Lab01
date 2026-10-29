# CMP 131 - Week 7 Lab 1
# Sum of Numbers

print("===== SUM OF NUMBERS =====")

number = int(input("Enter a positive number: "))

while number <= 0:
    print("Invalid number please try again")
    number = int(input("Try again: "))

total = 0
current_num = 1

while current_num <= number:
    total += current_num
    current_num += 1

print("==========================")
print(f"Number entered: {number}")
print(f"Total sum: {total}")
print("==========================")