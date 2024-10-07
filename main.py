from calculator import Calculator
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

# REPL function
def repl():
    calculator = Calculator()

    # Command mappings
    commands = {
        "add": AddCommand,
        "subtract": SubtractCommand,
        "multiply": MultiplyCommand,
        "divide": DivideCommand,
    }

    # Display menu function
    def display_menu():
        print("\nAvailable commands:")
        for command in commands:
            print(f" - {command}")
        print("\nExample input: 5 3 add")

    # Display the menu when the application starts
    display_menu()

    while True:
        user_input = input("\nEnter command (e.g., 5 3 add) or 'menu' to see options or 'exit' to quit: ").strip().lower()

        if user_input == "exit":
            print("Exiting the calculator. Goodbye!")
            break
        elif user_input == "menu":
            display_menu()
            continue

        try:
            value1, value2, operation = user_input.split()

            # Convert values to floats
            value1 = float(value1)
            value2 = float(value2)

            # Check if the operation is valid
            if operation not in commands:
                print("Invalid operation. Type 'menu' to see available commands.")
                continue

            # Execute the command
            command_class = commands[operation]
            command_instance = command_class(calculator, value1, value2)
            result = command_instance.execute()

            print(f"Result: {result}")

        except ValueError:
            print("Invalid input. Please enter valid numbers and an operation.")
        except ZeroDivisionError:
            print("Error: Division by zero.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Starting the REPL
if __name__ == "__main__":
    repl()
