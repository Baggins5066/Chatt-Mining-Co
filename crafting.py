class CraftingSystem:
    def __init__(self, resources):
        self.resources = resources
        self.recipes = {
            'pickaxe': {'ore': 2, 'wood': 1},
            'torch': {'coal': 1, 'wood': 1}
        }
    def craft(self):
        print("Available recipes:")
        for item, recipe in self.recipes.items():
            print(f"{item}: {recipe}")
        choice = input("Craft what? ")
        if choice in self.recipes:
            if self.resources.consume(self.recipes[choice]):
                return choice
            else:
                print("Not enough resources.")
                return None
        else:
            print("Invalid recipe.")
            return None
