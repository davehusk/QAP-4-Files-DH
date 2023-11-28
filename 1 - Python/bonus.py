'''
Dave Husk
dave.husk@keyin.com

QAP4 - Project 1 - BONUS


Loading this will give you three multiple choice, 
1. Uses Demo data, so you don't have to type
2. You fill it in
3. EXIT
'''

import matplotlib.pyplot as plt

# Define the months on the x-axis
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Predefined demo sales data
demo_sales = [2000, 3000, 2500, 1500, 3000, 4000, 3500, 3000, 4000, 4500, 3500, 3200]

def get_sales_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input == '':
            return 0.0
        try:
            value = float(user_input)
            if value < 0:
                raise ValueError("Sales cannot be negative. Please try again.")
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number or press Enter for $0.")

def plot_sales(sales):
    plt.figure(figsize=(10, 5))
    plt.plot(months, sales, marker='o')
    plt.title("Monthly Sales Data")
    plt.xlabel("Month")
    plt.ylabel("Total Sales ($)")
    plt.grid(True)
    plt.show()

def main():
    """
    The main function of the Monthly Sales Data Visualizer program.
    Allows the user to choose between using demo data, inputting their own sales data, or exiting the program.
    """
    print("\nWelcome to the Monthly Sales Data Visualizer!\n")
    print("1. Use demo data")
    print("2. Input your own sales data")
    print("3. Exit\n")

    choice = input("Choose an option (1, 2, or 3): ")
    if choice == '1':
        print("\nUsing demo sales data...\n")
        plot_sales(demo_sales)
    elif choice == '2':
        sales = []
        print("\nPlease enter your sales data:\n")
        for month in months:
            sales_input = get_sales_input(f"Enter the total sales for {month} (Press Enter for $0): ")
            sales.append(sales_input)
        plot_sales(sales)
    elif choice == '3':
        print("\nExiting the application. Goodbye!")
        return
    else:
        print("\nInvalid choice. Please run the program again to make a valid selection.")

if __name__ == "__main__":
    main()
