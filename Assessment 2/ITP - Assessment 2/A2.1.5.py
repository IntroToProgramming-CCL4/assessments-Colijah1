import random

# Define the Scentsational Vending machine class
class Scentsational_Vending:
    def __init__(self):
        # Initialize the conversion rate (for AED) and fragrance catalog with price and stock data
        self.conversion_rate = 3.67
        self.fragrances = {
            "Floral": {
                "Chanel No. 5": {"price": 105.00, "stock": 5},
                "Yves Saint Laurent Libre": {"price": 120.00, "stock": 3},
                "Gucci Bloom": {"price": 115.00, "stock": 4},
                "Viktor & Rolf Flowerbomb": {"price": 130.00, "stock": 2},
            },
            "Woody-Spicy": {
                "Dior Sauvage": {"price": 95.00, "stock": 6},
                "Paco Rabanne 1 Million": {"price": 95.00, "stock": 3},
                "Bleu de Chanel": {"price": 115.00, "stock": 1},
            },
            "Fruity": {
                "Creed Aventus": {"price": 320.00, "stock": 2},
            },
            "Oriental Floral": {
                "Tom Ford Black Orchid": {"price": 145.00, "stock": 0},  # Out of stock example
            },
            "Oriental Spicy": {
                "Armani Code": {"price": 90.00, "stock": 5},
            },
            "Woody Aromatic": {
                "Jean Paul Gaultier Le Male": {"price": 85.00, "stock": 7},
            },
        }
        self.loyalty_points = 0  # Initialize loyalty points
        self.currency = "USD"  # Default currency is USD

    # Ask user to choose the currency (USD or AED)
    def ask_for_currency(self):
        while True:
            print("\nChoose your currency:")
            print("1. USD")
            print("2. AED")
            choice = input("Enter 1 or 2: ").strip()
            if choice == "1":
                self.currency = "USD"
                print("\nCurrency set to USD.\n")
                break
            elif choice == "2":
                self.currency = "AED"
                print("\nCurrency set to AED.\n")
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

    # Display fragrance categories
    def show_menu(self):
        print("\n--- Welcome to Scentsational Vending! ---")
        print("Please select a fragrance category:\n")
        categories = list(self.fragrances.keys())
        for i, category in enumerate(categories, 1):
            print(f"{i:<2}. {category}")
        print()

    # Display fragrances within a selected category
    def show_fragrances_in_category(self, category):
        print(f"\n--- {category} Fragrances ---\n")
        for i, (fragrance, details) in enumerate(self.fragrances[category].items(), 1):
            # Display fragrance price and availability
            price_display = details["price"]
            if self.currency == "AED":
                price_display *= self.conversion_rate  # Convert price if in AED
            stock_status = (
                "Out of Stock"
                if details["stock"] == 0
                else f"In Stock: {details['stock']}"
            )
            print(f"{i:<2}. {fragrance:<30} {self.currency} {price_display:>8.2f}  ({stock_status})")
        print()

    # Handle the fragrance selection process (category, fragrance, quantity)
    def get_fragrance_choice(self):
        try:
            category_choice = int(input("Enter the number corresponding to the fragrance category: "))
            categories = list(self.fragrances.keys())
            if category_choice < 1 or category_choice > len(categories):
                print("\nInvalid category choice.\n")
                return None, None, 0
            selected_category = categories[category_choice - 1]
            self.show_fragrances_in_category(selected_category)

            fragrance_choice = int(input("Enter the number corresponding to the fragrance you'd like to buy: "))
            fragrances_in_category = list(self.fragrances[selected_category].keys())
            if fragrance_choice < 1 or fragrance_choice > len(fragrances_in_category):
                print("\nInvalid fragrance selection.\n")
                return None, None, 0
            fragrance_name = fragrances_in_category[fragrance_choice - 1]

            quantity = int(input(f"How many units of {fragrance_name} would you like to buy? "))
            fragrance_stock = self.fragrances[selected_category][fragrance_name]["stock"]

            if quantity > fragrance_stock:
                print(f"\nSorry, we only have {fragrance_stock} units of {fragrance_name} in stock.\n")
                return None, None, 0
            elif quantity < 1:
                print("\nYou must buy at least 1 unit.\n")
                return None, None, 0

            return selected_category, fragrance_name, quantity
        except ValueError:
            print("\nInvalid input. Please enter a valid number.\n")
            return None, None, 0

    # Handle payment processing and applying loyalty points
    def process_payment(self, fragrance_price, quantity):
        total_price = fragrance_price * quantity
        print("\n--- Loyalty Points Promo ---")
        print(f"You have {self.loyalty_points} loyalty points.\n")

        while True:
            print("Would you like to apply your points for a discount?")
            print("1. Yes")
            print("2. No")
            use_points = input("Enter 1 or 2: ").strip()

            if use_points == "1":
                if self.loyalty_points > 0:
                    discount_chance = random.randint(1, 100)
                    if discount_chance <= 50:  # 50% chance to apply discount
                        discount = min(self.loyalty_points, total_price)
                        total_price -= discount
                        self.loyalty_points -= int(discount)
                        print(f"\nLoyalty points applied! Discount: {self.currency} {discount:.2f}\n")
                        break
                    else:
                        print("\nPromo didn't activate. Try again on your next purchase!\n")
                        break
                else:
                    print("\nYou have no loyalty points to apply.\n")
                    break
            elif use_points == "2":
                print("\nLoyalty points not applied.\n")
                break
            else:
                print("\nInvalid choice. Please enter 1 or 2.\n")

        print(f"Total price after any discount: {self.currency} {total_price:.2f}\n")

        total_inserted = 0.0
        # Handle payment insertion
        while total_inserted < total_price:
            try:
                amount = float(input(f"Insert money for {self.currency} {total_price - total_inserted:.2f}: "))
                total_inserted += amount
                if total_inserted >= total_price:
                    return total_inserted
                else:
                    print(f"Insufficient amount. Total inserted: {self.currency} {total_inserted:.2f}")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Generate a detailed receipt for the transaction
    def generate_receipt(self, fragrance, category, fragrance_price, quantity, money_inserted, change):
        # Print the detailed receipt
        print("\n--- Receipt ---")
        print(f"Category: {category}")
        print(f"Fragrance: {fragrance}")
        print(f"Price per unit: {self.currency} {fragrance_price:.2f}")
        print(f"Quantity: {quantity}")
        print(f"Total Price: {self.currency} {fragrance_price * quantity:.2f}")
        print(f"Amount Paid: {self.currency} {money_inserted:.2f}")
        print(f"Change Returned: {self.currency} {change:.2f}")
        print(f"Loyalty Points Earned: {int(fragrance_price * quantity)}")
        print("Thank you for your purchase!")
        print("----------------------------")

    # Dispense the selected fragrance and update the inventory and loyalty points
    def dispense_fragrance(self, fragrance, category, fragrance_price, quantity, money_inserted):
        total_price = fragrance_price * quantity
        change = money_inserted - total_price
        print(f"\nDispensing {quantity} unit(s) of {fragrance}. Enjoy!")
        self.fragrances[category][fragrance]["stock"] -= quantity
        if change > 0:
            print(f"Change: {self.currency} {change:.2f}")
        self.loyalty_points += int(fragrance_price * quantity)
        print(f"Loyalty Points: {self.loyalty_points}\n")

        # Generate receipt for the transaction
        self.generate_receipt(fragrance, category, fragrance_price, quantity, money_inserted, change)

    # Main function to run the vending machine system
    def run(self):
        self.ask_for_currency()  # Ask for the user's currency preference
        while True:
            self.show_menu()  # Display the fragrance categories
            category, fragrance, quantity = self.get_fragrance_choice()  # Get user's fragrance selection
            if category and fragrance and quantity:
                fragrance_price = self.fragrances[category][fragrance]["price"]
                if self.currency == "AED":
                    fragrance_price *= self.conversion_rate  # Adjust price for AED
                payment = self.process_payment(fragrance_price, quantity)  # Process payment
                if payment is not None:
                    self.dispense_fragrance(fragrance, category, fragrance_price, quantity, payment)  # Dispense fragrance

            # Ask if the user wants to make another purchase
            print("\nWould you like to buy another fragrance?")
            print("1. Yes")
            print("2. No")
            another = input("Enter 1 or 2: ").strip()
            if another == "2":
                print("\nThank you for using Scentsational Vending!")
                break

# Create and run the vending machine
Vending_Machine = Scentsational_Vending()
Vending_Machine.run()
