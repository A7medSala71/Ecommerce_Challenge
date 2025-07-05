
# 🛒 E-commerce Checkout System

A simple object-oriented Python project that simulates an e-commerce shopping cart, checkout system, and customer balance management.

## 📂 Project Structure

```
Ecommerce_Challenge/
├── main.py              # Main script containing classes and checkout logic
├── venv/                # Python virtual environment
├── .idea/               # PyCharm project settings
```

## 🚀 Features

- Add products to cart
- Check for product expiration and stock levels
- Calculate subtotal, shipping cost, and total
- Handle customer balance during checkout
- Print receipt and shipment details

## 🧾 Classes Overview

- `Product`: Represents each product with price, weight, and shipping/expiration flags
- `Cart_Items`: Links a product with a quantity in the cart
- `Cart`: Manages all items in the shopping cart
- `Cust`: Represents the customer and their account balance
- `checkout()`: Finalizes the purchase, deducts balance, and prints receipt

## 📦 Sample Output

```
Shipment notice
2x Cheese 200g
1x Biscuits 700g
Total package weight 1.1kg
Checkout receipt
2x Cheese 200
1x Biscuits 150
1x Scratch Card 50
----------------------
Subtotal 400
Shipping 20
Amount 420
Customer balance 580
```

## 🛠️ Requirements

- Python 3.x
- (Optional) PyCharm for development

## ▶️ How to Run

```bash
python main.py
```

> Make sure your virtual environment is activated if needed.


## 👨‍💻 Author

Ahmed Salah  

---
