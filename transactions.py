import json
import uuid
from pathlib import Path

DB_PATH = Path(__file__).parent / 'db.json'


class Transaction:
    def __init__(self):
        self.transactions = []

    def load_transactions(self):
        if DB_PATH.exists():
            with open(DB_PATH, 'r') as f:
                data = json.load(f)
                self.transactions = data.get('transactions', [])

    def save_transactions(self):
        if DB_PATH.exists():
            with open(DB_PATH, 'r') as f:
                data = json.load(f)
        else:
            data = {}

        data['transactions'] = self.transactions
        with open(DB_PATH, 'w') as f:
            json.dump(data, f, indent=4)

    def add_transaction(self, details, amount, category):
        transaction = {
            'id': str(uuid.uuid4()),
            'details': details,
            'amount': amount,
            'category': category
        }
        self.transactions.append(transaction)
        self.save_transactions()
        print(f"Transaction '{details}' added successfully.")

    def list_transactions(self):
        if not self.transactions:
            print("No transactions available.")
        else:
            print("Transactions:")
            for trans in self.transactions:
                print(f"- {trans['details']} | Amount: {trans['amount']
                                                        } | Category: {trans['category']}")

    def calculate_balance(self):
        balance = sum(trans['amount'] for trans in self.transactions)
        print(f"Total Balance: {balance}")
