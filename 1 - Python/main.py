'''
Dave Husk
dave.husk@keyin.com

QAP4 - Project 1
'''

# One Stop Insurance Company needs a program to enter and calculate new insurance policy 
# information for its customers. Allow the program to repeat to allow the user to enter as many customers 
# as they want. Add at least 3 functions to the program. I will acc


import datetime
import re

# Constants
BASE_RATE = 869.00
ADDITIONAL_CAR_DISCOUNT = 0.25
EXTRA_LIABILITY_COST = 130.00
GLASS_COVERAGE_COST = 86.00
LOANER_CAR_COST = 58.00
HST_RATE = 0.15
PROCESSING_FEE = 39.99
DEFAULT_POLICY_NUMBER = 1944

# Validate input
def get_validated_input(prompt, default=None, validation_func=lambda x: True, format_func=lambda x: x):
    user_input = input(prompt)
    if user_input == '' and default is not None:
        user_input = default
        print(f"{default} (default)")
    formatted_input = format_func(user_input)
    if formatted_input and validation_func(formatted_input):
        return formatted_input
    else:
        print("Invalid input. Please try again.")
        return get_validated_input(prompt, default, validation_func, format_func)

def validate_phone_number(phone):
    # Remove all non-digit characters for validation
    digits_only = re.sub(r'\D', '', phone)
    # Check if we have exactly 10 digits
    if len(digits_only) == 10:
        # Format the string to the desired phone number format
        return f"{digits_only[:3]}-{digits_only[3:6]}-{digits_only[6:]}"
    else:
        return None

# Function to validate Canadian postal codes
def validate_postal_code(postal_code):
    # Canadian postal code pattern
    pattern = re.compile(r"[ABCEGHJKLMNPRSTVXY]\d[ABCEGHJKLMNPRSTVWXYZ] \d[ABCEGHJKLMNPRSTVWXYZ]\d")
    return pattern.match(postal_code.upper()) is not None

# Validate province
def validate_province(province):
    return province.upper() in ['ON', 'QC', 'NS', 'NB', 'MB', 'BC', 'PE', 'SK', 'AB', 'NL']

# Validate payment method
def validate_payment_method(method):
    return method.upper() in ['F', 'M', 'D']

# Validate currency
def format_currency(value):
    return "${:,.2f}".format(value)

# Validate number of cars
def validate_number_of_cars(input_str):
    return input_str.isdigit() and int(input_str) > 0

def calculate_insurance_premium(num_cars, extra_liability, glass_coverage, loaner_car):
    # Calculate base premium for the first car
    premium = BASE_RATE
    # Add premium for additional cars with a discount
    if num_cars > 1:
        premium += (num_cars - 1) * BASE_RATE * (1 - ADDITIONAL_CAR_DISCOUNT)
    
    # Add costs for selected options
    if extra_liability == 'Y':
        premium += EXTRA_LIABILITY_COST * num_cars
    if glass_coverage == 'Y':
        premium += GLASS_COVERAGE_COST * num_cars
    if loaner_car == 'Y':
        premium += LOANER_CAR_COST * num_cars

    return premium

# HST
def calculate_hst(premium):
    return premium * HST_RATE

# Monthly payment
def calculate_monthly_payment(premium, down_payment):
    total_cost = premium + calculate_hst(premium)
    if down_payment > 0:
        total_cost -= down_payment
    total_cost += PROCESSING_FEE  # Add processing fee
    return total_cost / 8  # Divide over 8 months

# Welcome message
print("\nWelcome to the One Stop Insurance Company Policy Calculator!\n\n** Demo: Pressing enter will work...\n")

def main():
    """
    This function collects customer information, calculates insurance premium, and displays the insurance policy summary.
    It prompts the user for various inputs such as customer's name, address, phone number, number of cars insured,
    extra liability coverage, glass coverage, loaner car option, and payment method.
    It validates the inputs and calculates the insurance premium based on the inputs.
    It also calculates the HST (Harmonized Sales Tax) and the total premium.
    If the payment method is monthly or down payment, it calculates the monthly payment as well.
    Finally, it displays the insurance policy summary including the customer information, premium details, and previous claims.
    """
    # Get customer info with validation and default values
    first_name = get_validated_input("Enter customer's first name: ", default="Dave").title()
    last_name = get_validated_input("Enter customer's last name: ", default="Husk").title()
    address = get_validated_input("Enter customer's address: ", default="69 Isthe Way Blvd")
    city = get_validated_input("Enter customer's city: ", default="Marystown").title()
    province = get_validated_input("Enter customer's province (e.g., NL, NS, NB): ", default="NL", validation_func=validate_province)
    
    postal_code = get_validated_input("Enter customer's postal code: ", default="A1A 1A1", validation_func=validate_postal_code)
    if not validate_postal_code(postal_code):
        print("Invalid postal code. Please try again.")
    else:
        print("Postal code is valid.")
        
    phone_number = get_validated_input(
        "Enter customer's phone number (e.g., 123-456-7890 or 1234567890): ",
        default="709-631-7414",
        validation_func=lambda x: x is not None,
        format_func=validate_phone_number
    )
    print(f"Phone number entered: {phone_number}")
    
    num_cars = int(get_validated_input("Number of cars insured: ", default="1", validation_func=validate_number_of_cars))
    extra_liability = get_validated_input("Extra liability coverage (Y/N): ", default="Y", validation_func=lambda x: x.upper() in ['Y', 'N']).upper()
    glass_coverage = get_validated_input("Glass coverage (Y/N): ", default="Y", validation_func=lambda x: x.upper() in ['Y', 'N']).upper()
    loaner_car = get_validated_input("Loaner car option (Y/N): ", default="Y", validation_func=lambda x: x.upper() in ['Y', 'N']).upper()

    # Inside main function:
    payment_method_input = get_validated_input("Payment method (F=Full, M=Monthly, D=Down Pay): ", default="F", validation_func=validate_payment_method).upper()
    payment_method = {'F': 'Full', 'M': 'Monthly', 'D': 'Down Pay'}[payment_method_input]

    down_payment = 0.0
    if payment_method_input == 'D':
        down_payment = float(get_validated_input("Enter the amount of the down payment: ", default="0", validation_func=lambda x: x.replace('.', '', 1).isdigit()))

    # Calculate insurance premium
    premium = calculate_insurance_premium(num_cars, extra_liability, glass_coverage, loaner_car)
    hst = calculate_hst(premium)
    total_premium = premium + hst

    # Calculate monthly payment if applicable
    monthly_payment = 0.0
    if payment_method_input == 'M':
        monthly_payment = calculate_monthly_payment(premium, down_payment)
    elif payment_method_input == 'D':
        monthly_payment = calculate_monthly_payment(premium - down_payment, 0)
        
    # Display results
    print("\n\n--- Insurance Policy Summary ---\n")
    print(f"Policy Number: {DEFAULT_POLICY_NUMBER}")
    print(f"Customer: {first_name} {last_name}")
    print(f"Address: {address}, {city}, {province.upper()}, {postal_code}")
    print(f"Phone: {phone_number}\n")
    print(f"Total Premium: {format_currency(total_premium)}")
    print(f"HST (15%): {format_currency(hst)}")
    if payment_method != "Full":
        print(f"Monthly Payment: {format_currency(monthly_payment)}")
        print(f"Down Payment: {format_currency(down_payment)}")

    # Example of displaying claims
    print("\nPrevious Claims:")
    print(f"{'Claim #':<10} {'Claim Date':<15} {'Amount':<15}")
    print("-" * 40)
    # Replace with actual claims list
    for i, claim in enumerate([("2023-01-01", 300), ("2023-06-15", 500), ("2023-08-24", 750)], start=1):
        print(f"{i:<10} {claim[0]:<15} {format_currency(claim[1]):<15}")

    print("\nThank you for using the One Stop Insurance Company Policy Calculator.")

# Main app
if __name__ == "__main__":
    main()
