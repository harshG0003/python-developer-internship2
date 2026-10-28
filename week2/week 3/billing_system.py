class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity

class Bill:
    def __init__(self, tax_rate=5):
        self.products = []
        self.tax_rate = tax_rate

    def add_product(self, product):
        self.products.append(product)

    def calculate_subtotal(self):
        return sum(product.get_total() for product in self.products)

    def calculate_tax(self):
        return self.calculate_subtotal() * self.tax_rate / 100

    def calculate_total(self):
        return self.calculate_subtotal() + self.calculate_tax()

    def display_bill(self):
        if not self.products:
            print("No products added to the bill.")
            return

        print("\n" + "=" * 68)
        print("                         SHOP BILL")
        print("=" * 68)
        print(f"{'Product':<20}{'Price':>12}{'Quantity':>12}{'Total':>16}")
        print("-" * 68)

        for product in self.products:
            print(
                f"{product.name:<20}"
                f"Rs. {product.price:>8.2f}"
                f"{product.quantity:>12}"
                f"Rs. {product.get_total():>12.2f}"
            )

        print("-" * 68)
        print(f"{'Subtotal:':>48} Rs. {self.calculate_subtotal():>10.2f}")
        print(
            f"{'Tax (' + str(self.tax_rate) + '%):':>48}"
            f" Rs. {self.calculate_tax():>10.2f}"
        )
        print(f"{'Grand Total:':>48} Rs. {self.calculate_total():>10.2f}")
        print("=" * 68)

def main():
    bill = Bill(tax_rate=18)
    
    print("--- Billing System ---")
    print("Enter product details. Type 'done' when finished.")
    while True:
        name = input("\nProduct name: ").strip()

        if name.lower() == "done":
            break
        if not name:
            print("Product name cannot be empty.")
            continue
        try:
            price = float(input("Price (Rs.): "))
            quantity = int(input("Quantity: "))

            if price < 0 or quantity <= 0:
                print("Price cannot be negative and quantity must be positive.")
                continue

            product = Product(name, price, quantity)
            bill.add_product(product)
            print("Product added successfully.")

        except ValueError:
            print("Invalid input. Enter a valid price and whole-number quantity.")
    bill.display_bill()

if __name__ == "__main__":
    main()
