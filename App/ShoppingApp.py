class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cart = Cart()

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.is_admin = True

class Category:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def update_category(self, new_name):
        self.name = new_name

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product, quantity):
        self.items.append({'product': product, 'quantity': quantity})

    def remove_from_cart(self, product):
        self.items = [item for item in self.items if item['product'] != product]

    def view_cart(self):
        for item in self.items:
            print(f"Product: {item['product'].name}, Quantity: {item['quantity']}, Price: {item['product'].price * item['quantity']}")

class Payment:
    def process_payment(self, method, amount):
        if method == 'UPI':
            return f"Paid {amount} via UPI."
        elif method == 'Debit Card':
            return f"Paid {amount} via Debit Card."
        else:
            return "Invalid payment method."

class ECommerceApp:
    def __init__(self):
        self.users = []
        self.categories = []

    # User Registration and Login
    def register_user(self, username, password):
        user = User(username, password)
        self.users.append(user)
        print(f"User {username} registered successfully!")

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                print(f"User {username} logged in successfully!")
                return user
        print("Invalid credentials!")
        return None

    # Public Login (Non-registered users)
    def public_login(self):
        return User("guest", "")

    # Admin-specific: Add/Update Category
    def add_category(self, name):
        category = Category(name)
        self.categories.append(category)
        print(f"Category {name} added successfully!")

    def update_category(self, old_name, new_name):
        for category in self.categories:
            if category.name == old_name:
                category.update_category(new_name)
                print(f"Category {old_name} updated to {new_name}!")
                return
        print(f"Category {old_name} not found!")

    # View Categories and Products
    def view_categories(self):
        if not self.categories:
            print("No categories available.")
        for category in self.categories:
            print(f"Category: {category.name}")
            for product in category.products:
                print(f" - {product.name}: {product.price}")

    # Cart Operations
    def add_item_to_cart(self, user, product_name, quantity):
        for category in self.categories:
            for product in category.products:
                if product.name == product_name:
                    user.cart.add_to_cart(product, quantity)
                    print(f"{quantity} of {product_name} added to cart!")
                    return
        print(f"Product {product_name} not found!")

    def remove_item_from_cart(self, user, product_name):
        for item in user.cart.items:
            if item['product'].name == product_name:
                user.cart.remove_from_cart(item['product'])
                print(f"{product_name} removed from cart!")
                return
        print(f"Product {product_name} not in cart!")

    def view_cart(self, user):
        user.cart.view_cart()

    # Payment Processing
    def checkout(self, user, payment_method):
        total = sum(item['product'].price * item['quantity'] for item in user.cart.items)
        payment = Payment()
        print(payment.process_payment(payment_method, total))
        user.cart.items.clear()

# Example usage:
app = ECommerceApp()

# Register and login as an admin
app.register_user('admin', 'admin123')
admin = app.login('admin', 'admin123')

# Add categories and products (only admin can do this)
app.add_category('Footwear')
app.add_category('Electronics')
app.categories[0].add_product(Product('Nike Shoes', 1200, 'Footwear'))
app.categories[1].add_product(Product('Smartphone', 15000, 'Electronics'))

# Login as a normal user
app.register_user('user1', 'password1')
user = app.login('user1', 'password1')

# Browse categories and add products to cart
app.view_categories()
app.add_item_to_cart(user, 'Nike Shoes', 2)
app.add_item_to_cart(user, 'Smartphone', 1)

# View cart and checkout
app.view_cart(user)
app.checkout(user, 'UPI')

# Public user access
guest_user = app.public_login()
app.add_item_to_cart(guest_user, 'Nike Shoes', 1)
app.view_cart(guest_user)
app.checkout(guest_user, 'Debit Card')
