from operations import Operations


def menu():
    print("1 - Add Category")
    print("2 - Add Transaction")
    print("3 - List Transactions")
    print("4 - Calculate Balance")
    print("5 - Exit")


def main():
    operations = Operations()

    while True:
        menu()
        choice = input("Choose an option: ")
        operations.clear_screen()

        if choice == '1':
            operations.add_category()
        elif choice == '2':
            operations.add_transaction()
        elif choice == '3':
            operations.list_transactions()
        elif choice == '4':
            operations.calculate_balance()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
