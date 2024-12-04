from datetime import datetime

log_file = "vinu.txt"

def log_message(message):
    with open(log_file, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - {message}\n")

def divide_numbers():
    try:
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))
        result = num1 / num2
        print(f"The result is: {result}")

    except ZeroDivisionError:
        error_message = "Error: Division by zero is not allowed."
        print(error_message)
        log_message(error_message)

    except ValueError:
        error_message = "Error: Invalid input. Please enter numeric values."
        print(error_message)
        log_message(error_message)

    except Exception as e:
        error_message = f"Unexpected error: {str(e)}"
        print(error_message)
        log_message(error_message)

divide_numbers()