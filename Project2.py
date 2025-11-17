# Vending Machine Project
# Name: Natally Chaves :)
# This program simulates a vending machine using objects.

class Beverage:
    def __init__(self, name, price):
        # drink name and price
        self.name = name
        self.price = price

    def __str__(self):
        # how the drink shows up in the menu
        return f"{self.name} - ${self.price:.2f}"


class VendingMachine:
    def __init__(self, beverages):
        # list of Beverage objects
        self.beverages = beverages

    def display_menu(self):
        # show all drink options
        print("\n===== VENDING MACHINE =====")
        for i, drink in enumerate(self.beverages, start=1):
            print(f"{i}) {drink}")
        print("=====================================")

    def get_selection(self):
        # get a valid drink number from the user
        while True:
            try:
                choice = int(input("Pick a drink number: "))
                if 1 <= choice <= len(self.beverages):
                    return self.beverages[choice - 1]
                else:
                    print("Please pick a number from the menu.")
            except ValueError:
                print("Please enter a whole number.")

    def collect_money(self, beverage):
        # keep asking for money until we have enough
        total = 0.0
        print(f"\nYou chose: {beverage.name} for ${beverage.price:.2f}")

        while total < beverage.price:
            print(f"Still need: ${beverage.price - total:.2f}")
            try:
                amount = float(input("Insert money (e.g. 1.00, 0.50): "))
                if amount > 0:
                    total += amount
                else:
                    print("Amount must be positive.")
            except ValueError:
                print("Please enter a valid number.")
        # return change (could be 0.0)
        return total - beverage.price

    def vend(self, beverage):
        # pretend to give the drink
        print(f"\nVending your {beverage.name}...")

    def run(self):
        # main vending machine loop (does not stop)
        print("Welcome to the Colombian Vending Machine!")
        print("Press Ctrl+C to quit.\n")

        while True:
            self.display_menu()
            drink = self.get_selection()
            change = self.collect_money(drink)
            self.vend(drink)

            if change > 0:
                print(f"Your change: ${change:.2f}")

            print("Thanks for buying!\n" + "-" * 35)


if __name__ == "__main__":
    # Colombian drink options ( make it a bit more original)
    drink1 = Beverage("Agua", 1.00)
    drink2 = Beverage("Colombiana", 1.75)
    drink3 = Beverage("Pony Malta", 2.00)
    drink4 = Beverage("Jugo Hit Mango", 1.80)
    drink5 = Beverage("Kumis", 2.25)
    drink6 = Beverage("Manzana Postobón", 1.85)  # coffee changed to Manzana

    drinks = [drink1, drink2, drink3, drink4, drink5, drink6]

    machine = VendingMachine(drinks)
    machine.run()
