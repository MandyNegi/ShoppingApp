
categories = {
    "Footwear": {
        "1": "Nike Shoes: 1200rs",
        "2": "Puma Shoes: 1000rs",
        "3": "Rebook Shoes: 1000rs",
        "4": "ABS Shoes: 500rs"
    },
    "Electronics": {
        "1": "Smartphone: 12000rs",
        "2": "SmartWatch: 10000rs",
        "3": "Mobile Charge: 1000rs"
    },
    "Clothing": {
        "1": "Nike T-Shirt: 1200rs",
        "2": "Puma T-shirt: 1000rs",
        "3": "Adidas T-shirt: 1000rs"
    }
}

# Cart for users
user_cart = []

# User credentials (for simplicity, stored in code)
admin_credentials = {'username': 'admin', 'password': 'root'}


# Function to handle user login
def user_login():
    while True:
        guest = input('Enter A for Admin or U to Login as User (or Q to Quit): ').upper()
        if guest == 'U':
            print('User login successful...')
            user_operations()
        elif guest == 'A':
            admin_login()
        elif guest == 'Q':
            print("Exiting application...")
            break
        else:
            print("Invalid option!")


# Function for admin login
def admin_login():
    username = input('Enter Username: ')
    password = input('Enter Password: ')

    if username == admin_credentials['username'] and password == admin_credentials['password']:
        print('Admin login successful...')
        admin_operations()
    else:
        print('Wrong credentials!')


# Display categories and items dynamically
def display_categories():
    print("\nCategories:")
    for idx, cat_name in enumerate(categories, 1):
        print(f"{idx}: {cat_name}")


def display_items(category):
    if categories[category]:
        print(f"\nItems in {category}:")
        for item_id, item_name in categories[category].items():
            print(f"{item_id}: {item_name}")
    else:
        print(f"\nNo items in {category} yet.")


# Function to handle user operations
def user_operations():
    exit_condition = 'N'

    while exit_condition != 'Y':
        print("\n1: View Categories\n2: Check Cart\n3: Payment\n4: Logout")
        option = input("Please select an option: ")

        if option == '1':
            display_categories()
            category_choice = input("Select a category by number to view items: ")
            try:
                category = list(categories.keys())[int(category_choice) - 1]
                display_items(category)
                add_to_cart(category)
            except (IndexError, ValueError):
                print("Invalid category selection!")

        elif option == '2':
            view_cart()

        elif option == '3':
            process_payment()

        elif option == '4':
            print("Logging out...")
            exit_condition = 'Y'
        else:
            print("Invalid option!")


# Function to add items to the cart
def add_to_cart(category):
    item_id = input("\nPlease select an item number to add to the cart (or press 'B' to go back): ").upper()
    if item_id == 'B':
        return
    if item_id in categories[category]:
        user_cart.append(categories[category][item_id])
        print(f'{categories[category][item_id]} added to the cart.')
    else:
        print("Invalid item selection!")


# Function to view the cart
def view_cart():
    if not user_cart:
        print("Your cart is empty!")
    else:
        print("\nItems in your cart:")
        for idx, item in enumerate(user_cart, 1):
            print(f"{idx}: {item}")

        modify = input("Do you want to modify your cart? (Y/N): ").upper()
        if modify == 'Y':
            remove_item()


# Function to remove items from the cart
def remove_item():
    while user_cart:
        item_idx = input("\nEnter item number to remove (or press 'Y' to finalize payment): ").upper()

        if item_idx == 'Y':
            break
        else:
            try:
                item_idx = int(item_idx) - 1
                removed_item = user_cart.pop(item_idx)
                print(f"{removed_item} removed from the cart.")
            except (IndexError, ValueError):
                print("Invalid item number!")

    if not user_cart:
        print("Your cart is now empty.")


# Function to process payment
def process_payment():
    if not user_cart:
        print("Your cart is empty!")
        return

    print("\nItems in your cart for payment:")
    for idx, item in enumerate(user_cart, 1):
        print(f"{idx}: {item}")

    print("\nPayment Options:\n1: UPI\n2: Debit Card\n3: Credit Card")
    payment_method = input("Please select a payment method: ")

    if payment_method in ['1', '2', '3']:
        print("Payment successful! Thank you for your purchase.")
        user_cart.clear()  # Clear the cart after successful payment
    else:
        print("Invalid payment method!")


# Admin operations to add a new category and items
def admin_operations():
    while True:
        print("\nAdmin Options:\n1: Add New Category\n2: Add Items to Category\n3: View All Categories and Items\n4: Logout")
        admin_choice = input("Select an option: ")

        if admin_choice == '1':
            add_category()

        elif admin_choice == '2':
            add_items_to_category()

        elif admin_choice == '3':
            display_categories()
            category_choice = input("Select a category by number to view items: ")
            try:
                category = list(categories.keys())[int(category_choice) - 1]
                display_items(category)
            except (IndexError, ValueError):
                print("Invalid category selection!")

        elif admin_choice == '4':
            print("Admin logging out...")
            break
        else:
            print("Invalid option!")


# Function to add a new category
def add_category():
    new_category = input("Enter new category name: ").title()
    if new_category in categories:
        print("Category already exists!")
        return

    categories[new_category] = {}
    print(f"New category '{new_category}' added successfully!")
    add_items_to_category(new_category)  # Prompt admin to add items to the new category immediately


# Function to add items to an existing category
def add_items_to_category(existing_category=None):
    if not existing_category:
        display_categories()
        category_idx = input("Select category number to add items to: ")
        try:
            existing_category = list(categories.keys())[int(category_idx) - 1]
        except (IndexError, ValueError):
            print("Invalid category selection!")
            return

    print(f"\nAdding items to {existing_category} category:")
    while True:
        item_name = input("Enter item name (or type 'done' to finish): ").title()
        if item_name.lower() == 'done':
            break
        item_price = input(f"Enter price for '{item_name}': ")
        item_id = str(len(categories[existing_category]) + 1)
        categories[existing_category][item_id] = f"{item_name}: {item_price}rs"
        print(f"Item '{item_name}' added to {existing_category} category.")


# Start the application
def start_app():
    print("************ Welcome to the E-commerce Application ************")
    user_login()


# Run the application
if __name__ == '__main__':
    start_app()
