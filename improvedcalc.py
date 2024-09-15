def add(numbers):
    """Return the sum of a list of numbers."""
    return sum(numbers)

def sub(numbers):
    """Return the difference of a list of numbers."""
    if len(numbers) < 2:
        raise ValueError("Subtraction requires at least two numbers.")
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def mul(numbers):
    """Return the product of a list of numbers."""
    result = 1
    for num in numbers:
        result *= num
    return result

def div(numbers):
    """Return the division of a list of numbers."""
    if len(numbers) < 2:
        raise ValueError("Division requires at least two numbers.")
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result /= num
    return result

def main():
    try:
        num = list(map(int, input("Enter the numbers separated by spaces: ").split()))
        print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
        operation = int(input("Enter the operation number (1-4): "))
        
        if len(num) < 2 and operation != 1:
            print("Please enter at least two numbers for the operation.")
        elif operation == 1:
            print("Result:", add(num))
        elif operation == 2:
            print("Result:", sub(num))
        elif operation == 3:
            print("Result:", mul(num))
        elif operation == 4:
            print("Result:", div(num))
        else:
            print("Invalid operation number.")
    except ValueError as e:
        print("Error:", str(e))
    except ZeroDivisionError as e:
        print("Error:", str(e))