class Shop:
    def __init__(self, resources):
        self.resources = resources
        self.prices = {'pickaxe': 10, 'torch': 5}
        self.inventory = {'pickaxe': 0, 'torch': 0}
    def sell(self):
        print("Inventory:")
        for item, qty in self.inventory.items():
            print(f"{item}: {qty}")
        choice = input("Sell what? ")
        if choice in self.inventory and self.inventory[choice] > 0:
            self.inventory[choice] -= 1
            return self.prices[choice]
        else:
            print("You don't have that item.")
            return 0
    def add_item(self, item):
        if item in self.inventory:
            self.inventory[item] += 1
