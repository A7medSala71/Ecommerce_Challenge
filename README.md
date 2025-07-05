
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

## 🌐 Push to GitHub (Command Line Instructions)

1. Open Command Prompt and navigate to your project:

```bash
cd C:\Users\pc\PycharmProjects\Ecommerce_Challenge
```

2. Initialize a git repository (if not already done):

```bash
git init
```

3. Add your remote GitHub repository (replace `USERNAME` and `REPO_NAME`):

```bash
git remote add origin https://github.com/USERNAME/REPO_NAME.git
```

4. Stage all files for commit:

```bash
git add .
```

5. Commit your changes:

```bash
git commit -m "Initial commit: E-commerce checkout system"
```

6. Push the project to GitHub:

```bash
git push -u origin master
```

> 🔐 If you're asked to authenticate, use your GitHub username and [personal access token](https://github.com/settings/tokens) instead of your password.

---

## 👨‍💻 Author

Ahmed Salah  
Built with ❤️ using Python and PyCharm

---
