import os
from categories import Category
from transactions import Transaction


class Operations:
    def __init__(self):
        self.categories = Category()
        self.transactions = Transaction()
        self.categories.load_categories()
        self.transactions.load_transactions()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def add_category(self):
        category_name = input("Enter the new category name: ")
        self.categories.add_category(category_name)
        self.clear_screen()

    def add_transaction(self):
        details = input("Enter transaction details: ")

        while True:
            amount_str = input("Enter transaction amount: ")
            try:
                amount = float(amount_str)
                break
            except ValueError:
                print("Invalid amount. Please enter a valid number.")

        print("Choose a category:")
        self.categories.list_categories()

        while True:
            try:
                category_choice = int(
                    input("Enter the number of the category: ")) - 1
                if 0 <= category_choice < len(self.categories.categories):
                    category = self.categories.categories[category_choice]['category']
                    break
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        self.transactions.add_transaction(details, amount, category)
        self.clear_screen()

    def list_transactions(self):
        self.transactions.list_transactions()

    def calculate_balance(self):
        self.transactions.calculate_balance()
