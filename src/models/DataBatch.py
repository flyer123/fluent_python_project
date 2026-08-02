class DataBatch:

    def __init__(self, records):
        self.records = records

    def __getitem__(self, item):
        return self.records[item]

    def __iter__(self):
        return iter(self.records)

    def __len__(self):
        return len(self.records)

    def __bool__(self):
        return bool(len(self.records))

    def __repr__(self):
        return f"DataBatch(records={len(self.records)!r})"
