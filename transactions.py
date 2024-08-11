from dataclasses import dataclass, field
from typing import List


@dataclass
class Transactions:
    details: str
    value: float
    category: str
    transactions: List[dict] = field(default_factory=list)

    def register_transaction(self):
        new_transaction = vars(self)
        return new_transaction


t1 = Transactions("Teste", 1000, "Receita")

print(t1.register_transaction())
