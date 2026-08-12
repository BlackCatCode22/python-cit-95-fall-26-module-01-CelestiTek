# Pay Rate Calculator with Overtime (1.5x for hours > 40)

def calculate_gross_pay(hours, rate):
    """
    Calculate gross pay with overtime.
    Overtime is paid at 1.5x the hourly rate for hours over 40.
    """
    if hours > 40:
        regular_pay = 40 * rate
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * rate * 1.5
        return regular_pay + overtime_pay
    else:
        return hours * rate


def main():
    try:
        # Get user input
        hours_worked = float(input("Enter hours worked: "))
        hourly_rate = float(input("Enter hourly pay rate: "))

        # Validate inputs
        if hours_worked < 0 or hourly_rate < 0:
            print("Error: Hours and rate must be non-negative.")
            return

        # Calculate gross pay
        gross_pay = calculate_gross_pay(hours_worked, hourly_rate)

        # Display result
        print(f"Gross pay: ${gross_pay:,.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")


if __name__ == "__main__":
    main()
