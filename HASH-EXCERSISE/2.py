class InventoryHashTable:

    def __init__(self, size=10):
        self.size = size
        self.table = []
        for i in range(size):
            self.table.append([])

    def _hash(self, key):
        total = 0
        for ch in key:
            total = total + ord(ch)
        return total % self.size

    def set_item(self, sku, name, quantity):
        index = self._hash(sku)
        bucket = self.table[index]

        found = False
        for item in bucket:
            if item["sku"] == sku:
                item["name"] = name
                item["quantity"] = quantity
                found = True

        if found == False:
            bucket.append({"sku": sku, "name": name, "quantity": quantity})

    def get_item(self, sku):
        index = self._hash(sku)
        bucket = self.table[index]

        for item in bucket:
            if item["sku"] == sku:
                return item

        return None

    def remove_item(self, sku):
        index = self._hash(sku)
        bucket = self.table[index]

        i = 0
        while i < len(bucket):
            if bucket[i]["sku"] == sku:
                bucket.pop(i)
                return True
            i = i + 1

        return False

    def print_table(self):
        print("inventory:")
        i = 0
        while i < self.size:
            print("bucket", i, self.table[i])
            i = i + 1