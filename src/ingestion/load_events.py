import csv

def load_events(path):
    with open(path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        rows = [
            {
                **row, 
                "revenue": int(row["revenue"])
            }
            for row in reader
        ]
        return rows

