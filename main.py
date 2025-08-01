import time
from resources import ResourceManager
from crafting import CraftingSystem
from shop import Shop

def main():
    resources = ResourceManager()
    crafting = CraftingSystem(resources)
    shop = Shop(resources)
    money = 0
    print("Welcome to Chatt Mining Co!")
    while True:
        print(f"\nMoney: ${money}")
        print("Resources:", resources.status())
        print("1. Mine resources")
        print("2. Craft items")
        print("3. Sell items")
        print("4. Quit")
        choice = input("Choose an action: ")
        if choice == '1':
            mined = resources.mine()
            print(f"You mined: {mined}")
        elif choice == '2':
            crafted = crafting.craft()
            print(f"You crafted: {crafted}")
        elif choice == '3':
            earned = shop.sell()
            money += earned
            print(f"You earned ${earned}")
        elif choice == '4':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice.")
        time.sleep(1)

if __name__ == "__main__":
    main()
