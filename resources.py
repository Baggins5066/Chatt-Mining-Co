import random

class ResourceManager:
    def __init__(self):
        self.resources = {'ore': 0, 'coal': 0, 'wood': 0}
    def mine(self):
        mined = {r: random.randint(1, 3) for r in self.resources}
        for r, amt in mined.items():
            self.resources[r] += amt
        return mined
    def status(self):
        return self.resources.copy()
    def consume(self, recipe):
        for r, amt in recipe.items():
            if self.resources.get(r, 0) < amt:
                return False
        for r, amt in recipe.items():
            self.resources[r] -= amt
        return True
