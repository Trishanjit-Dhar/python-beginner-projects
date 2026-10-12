# Store every expense as a tuple: (amount, category, description).
Expenses = []

# Set the maximum amount the user plans to spend for the month.
budget_limit = 100000.00

print("WELCOME TO EXPENSE TRACKER")

# Keep showing the menu until the user chooses to exit.
while True :
    print("\n----MAIN MENU----")
    print("1. ADD EXPENSE")
    print("2. VIEW ALL EXPENSES")
    print("3. CHECK BUDGET AND SUMMARY")
    print("4. EXIT")

    # Read the menu option as text so it can be compared with "1", "2", etc.
    choice = input("Enter your required option here: ")


    if choice == "1":
        print("\n---ADDING NEW EXPENSE---")
        try:
            # Convert the entered amount to a number. Invalid values raise ValueError.
            Amount = float(input("Enter your expense here: "))
            Category = input("Enter where you spend your money: ")
            Description = input("Enter a small description about your expense: ")

            # Group the details for one expense, then save it to the expense list.
            expense_tuple = (Amount,Category,Description)

            Expenses.append(expense_tuple)

            print("Expense added successfully")
        except ValueError:
            print("Please enter an appropriate value in the amount section")


    elif choice == "2":
        print("\n---VIEWING ALL EXPENSES---")

        # Avoid displaying an empty list when the user has not added expenses yet.
        if len(Expenses) == 0 :
            print("No previous expense")

        else:
            # Number each saved expense starting from 1 and unpack its details.
            for index,item in enumerate(Expenses,start =1):
                Amount , Category , Description = item
                print(f"{index}|INR {Amount:.2f}|{Category}|{Description}")


    elif choice == "3":
        # Add the amount from every stored expense to calculate total spending.
        total_expenditure = 0.0
        for item in Expenses:
            amount = item[0]
            total_expenditure += amount

        print("\n---CHECKING BUDGET AND SUMMARY---")
        print(f"Total Spent: INR {total_expenditure:.2f}")
        print(f"Budget Limit: INR {budget_limit:.2f}")

        # Give a message based on how much of the budget has been used.
        if total_expenditure > budget_limit :
            print("ALERT ALERT \nYou have exceeded your monthly limit please do not spend any more money")

        elif total_expenditure >= (budget_limit * 0.8):
            print("Please spend your money wisely you have already exceeded 80 percent of your monthly limit")

        else:
            print("Congratulations to your selfcontrol you didn't over spend this month and your expenses are in your control")


    elif choice == "4":
        print("\nEXITING FROM THE TRACKER, THANKYOU FOR USING OUR EXPENSE TRACKER")
        # Stop the infinite menu loop and end the program.
        break


    else:
        # Handle anything other than the four valid menu options.
        print("TRY AGAIN \nPlease enter a valid choice from any of the provided four choices")
