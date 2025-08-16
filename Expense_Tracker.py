import csv
import os

FILE_NAME = "expenses.csv"

def add_expense(amount, category):
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category])
    print("✅ Expense added successfully!")

def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("❌ No expenses recorded yet.")
        return
    
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        print("\n📊 Your Expenses:")
        total = 0
        for row in reader:
            if row:
                print(f"💵 {row[0]} INR - {row[1]}")
                total += float(row[0])
        print(f"\n💰 Total Spent: {total} INR")

def menu():
    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            amount = input("Enter amount (INR): ")
            category = input("Enter category (Food/Travel/Other): ")
            add_expense(amount, category)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("👋 Exiting... Bye!")
            break
        else:
            print("⚠ Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
