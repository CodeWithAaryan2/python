import uuid

class Product:
    def __init__(self, name, price, stock):
        self.product_id = str(uuid.uuid4())[:8]
        self.name = name
        self.price = price
        self.stock = stock
    
    def update_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        else:
            print(f"⚠️ Insufficient stock for {self.name}")
            return False
    
    def __str__(self):
        return f"{self.name} - ₹{self.price} (Stock: {self.stock})"


class Customer:
    def __init__(self, name):
        self.customer_id = str(uuid.uuid4())[:8]
        self.name = name
        self.cart = ShoppingCart()
    
    def add_to_cart(self, product, quantity):
        self.cart.add_item(product, quantity)
    
    def checkout(self):
        self.cart.process_order()
    
    def __str__(self):
        return f"Customer: {self.name} (ID: {self.customer_id})"


class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, product, quantity):
        if product.update_stock(quantity):
            if product.product_id in self.items:
                self.items[product.product_id]["quantity"] += quantity
            else:
                self.items[product.product_id] = {"product": product, "quantity": quantity}
            print(f"✅ Added {quantity} x {product.name} to cart.")
    
    def calculate_total(self):
        total = sum(item["product"].price * item["quantity"] for item in self.items.values())
        return total
    
    def process_order(self):
        if not self.items:
            print("🛒 Cart is empty! Add items before checkout.")
            return
        print("\n🛍️   Processing Order...")
        for item in self.items.values():
            print(f"{item['quantity']} x {item['product'].name} - ₹{item['product'].price * item['quantity']}")
        print(f"💰 Total Amount: ₹{self.calculate_total()}")
        self.items.clear()
        print("✅ Order Placed Successfully!\n")


# Example Usage
p1 = Product("Laptop", 55000, 10)
p2 = Product("Mouse", 500, 20)
p3 = Product("Keyboard", 1500, 15)

c1 = Customer("Aaryan Sharma")
c1.add_to_cart(p1, 1)
c1.add_to_cart(p2, 2)
c1.add_to_cart(p3, 1)
c1.checkout()