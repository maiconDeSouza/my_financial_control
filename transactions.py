from uuid import uuid4


class Transactions:
    def __init__(self, details, value, category):
        self.id = str(uuid4())
        self.details = details
        self.value = value
        self.category = category
        self.transactions = []

    def register_transaction(self):
        new_transaction = {
            "id": self.id,
            "details": self.details,
            "value": self.value,
            "category": self.category
        }

        self.transactions.append(new_transaction)
        return new_transaction


t1 = Transactions("Teste", 1000, "Receita")

print(t1.register_transaction())
print(t1.transactions)
