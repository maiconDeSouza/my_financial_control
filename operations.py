from pathlib import Path
import json


class Operations:
    def __init__(self):
        self.transactions = []
        self.categories = []

    def access_json_file(self):
        file = Path("db.json")
        if file.exists():
            with open("db.json", "r") as f:
                res = f.read()
                db_str = json.loads(res)
        else:
            db_json = {
                "transactions": [],
                "categories": []
            }
            with open("db.json", "w",) as f:
                f.write(json.dumps(db_json, indent=2))


o = Operations()
o.access_json_file()
