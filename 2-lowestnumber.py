# Find the lowest number
# Create a program that ask 3 numbers. 
# Find the lowest number using only if-else statement.
# Display the lowest number


def comparison(first, second, third):
    if first > second and second < third:
        print(f"The lowest number is the second number, {second}.")
    elif third > first and second < first:
        print(f"The lowest number is the second number, {second}.")
    elif first > third and second > third:
        print (f"The lowest number is the third number, {third}.")
    elif second > third and second < first:
        print (f"The lowest number is the third number, {third}.")
    else:
        print (f"The lowest number is the first number, {first}.")
   

first = int(input("Enter the first number here: "))
second = int(input("Enter the second number here: "))
third = int(input("Enter the last number here: "))
    
display = comparison(first, second, third)