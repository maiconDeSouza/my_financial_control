import json
import uuid
from pathlib import Path

DB_PATH = Path(__file__).parent / 'db.json'


class Category:
    def __init__(self):
        self.categories = []

    def load_categories(self):
        if DB_PATH.exists():
            with open(DB_PATH, 'r') as f:
                data = json.load(f)
                self.categories = data.get('categories', [])

    def save_categories(self):
        if DB_PATH.exists():
            with open(DB_PATH, 'r') as f:
                data = json.load(f)
        else:
            data = {}

        data['categories'] = self.categories
        with open(DB_PATH, 'w') as f:
            json.dump(data, f, indent=4)

    def add_category(self, category_name):
        if any(cat['category'] == category_name for cat in self.categories):
            print(f"Category '{category_name}' already exists.")
        else:
            category = {
                'id': str(uuid.uuid4()),
                'category': category_name
            }
            self.categories.append(category)
            self.save_categories()
            print(f"Category '{category_name}' added successfully.")

    def list_categories(self):
        if not self.categories:
            print("No categories available.")
        else:
            print("Categories:")
            for index, cat in enumerate(self.categories, start=1):
                print(f"{index} - {cat['category']}")
