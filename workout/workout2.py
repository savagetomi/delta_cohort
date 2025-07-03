expenses = [
    ["Transportation", 85000],
    ["Food", 200000]
]

while True:
    option = input("1. Add expenses.\n2. View Expenses. \n3. Show total Expenses.\n4. Exit. \n(Choose 1 | 2 | 3 | 4 ): ")
    if option == "1":
        expenseName = input("Write your expense name: ")
        expenseAmount = input("Write your expense amount: ")
        expenses.append([expenseName, float(expenseAmount)])
        print("Expense has been duly noted")
        print(expenses)
    elif option == "2":
        for exp in expenses:
            print(f" {"--" * 21}\n Expense: {exp[0]}, Amount: {exp[1]}\n {"--" * 21}")
    elif option == "3":
        totalAmount = 0
        for exp in expenses:
            totalAmount += exp[1]
        else:
            if totalAmount == 0:
                print(f"{"--" * 21}\n You're a broke ass Nigga.Go Hustle Motherfucker.\n{"--" * 21}")
            print(f"{"--" * 21}\nYour Total Amount is {totalAmount}\n{"--" * 21}")
    elif option == "4":
        delle = expenses.remove(expenses[0])
        print(expenses)

    elif option == "5":
        choice = input("Are you sure you want to exit? ( Yes | No ): ")
        if choice == "Yes":
            print(f"{"--" * 21}\nLeaving the expense tracker.\n{"--" * 21}")
            break
        elif choice == "No":
            continue
    else:
        print("Invalid option. Write a number option above")