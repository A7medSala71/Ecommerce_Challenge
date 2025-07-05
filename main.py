class Product:
    def __init__(self, name, price, Qty, Is_expired=False, Is_shippable=False, Wght=0.0):
        self.name = name
        self.price = price
        self.Qty = Qty
        self.Is_expired = Is_expired
        self.Is_shippable = Is_shippable
        self.Wght = Wght

class Cart_Items:
    def __init__(self, product, qty):
        self.product = product
        self.qty = qty

class Cart:
    def __init__(self):
        self.Items = []

    def Is_empty(self):
        return len(self.Items) == 0

    def add(self, product, qty):
        if qty > product.Qty:
            print(f'Out of stock for {product.name}')
            return
        self.Items.append(Cart_Items(product, qty))

class Cust:
    def __init__(self, balance):
        self.balance = balance

def checkout(cust, cart):
    if cart.Is_empty():
        print('Cart is EMPTY')
        return

    SubTotal = 0.0
    Shipping = 0.0
    Shipment = []
    Total_Wght = 0.0

    for item in cart.Items:
        p = item.product

        if p.Is_expired:
            print(f"Error: Product {p.name} is expired")
            return

        if item.qty > p.Qty:
            print(f"Error: Not enough stock for {p.name}")
            return

        p.Qty -= item.qty
        SubTotal += item.qty * p.price

        if p.Is_shippable:
            Shipment.append(f"{item.qty}x {p.name} {int(p.Wght * 1000)}g")
            Shipping += 10
            Total_Wght += item.qty * p.Wght

    Total = SubTotal + Shipping

    if Total > cust.balance:
        print("Insufficient Balance")
        return

    cust.balance -= Total

    if Shipment:
        print("Shipment notice")
        for s in Shipment:
            print(s)
        print(f"Total package weight {Total_Wght:.1f}kg")

    print("Checkout receipt")
    for item in cart.Items:
        print(f"{item.qty}x {item.product.name} {item.qty * item.product.price:.0f}")
    print("----------------------")
    print(f"Subtotal {SubTotal:.0f}")
    print(f"Shipping {Shipping:.0f}")
    print(f"Amount {Total:.0f}")
    print(f"Customer balance {cust.balance:.0f}")

# Example usage
if __name__ == '__main__':
    cheese = Product("Cheese", 100, 5, Is_expired=False, Is_shippable=True, Wght=0.2)
    biscuits = Product("Biscuits", 150, 3, Is_expired=False, Is_shippable=True, Wght=0.7)
    scratch_card = Product("Scratch Card", 50, 10, Is_expired=False, Is_shippable=False)

    customer = Cust(1000)
    cart = Cart()

    cart.add(cheese, 2)
    cart.add(biscuits, 1)
    cart.add(scratch_card, 1)

    checkout(customer, cart)
