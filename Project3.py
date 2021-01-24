num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your secend number: "))


if num1 < 0 or num2 < 0:
    print("False")
else:
    print(f"Total = {num1 + num2}")
    print(f"Submission = {num1 - num2}")
    print(f"Multiplication = {num1 * num2}")
    print(f"Division = {int (num1 / num2)}")
    print(f"Left over = {num1 % num2}")
    print(f"Tavan = {num1 ** num2}")
    
    

