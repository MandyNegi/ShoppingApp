#  e-commerce application which has login and public login features
#  The applications that have been developed should also include categories, such as 3–4 for footwear, clothing, electronics,
#  It should be possible to add and update categories in the application
#  it must contain a feature that allows you to add or remove items from your cart
#  the program needs to support a variety of payment options, including UPI and debit cards
from tokenize import String

categoriesList = ['']
def get_input():

    footwear_list = {"1": "Nike Shoes: 1200rs", "2": "Puma Shoes: 1000rs", "3": "Rebook Shoes: 1000rs", "4": "ABS Shoes: 500rs"}
    electronics_list = {"1": "Smartphone: 12000rs","2": "SmartWatch: 10000rs","3": "Mobile Charge: 1000rs"}
    clothing_list = {"1": "Nike T-Shirt: 1200rs","2": "Puma T-shirt: 1000rs","3": "Adidas Tshirt: 1000rs"}
    exit_condition ='N'

    user_cart = []
    category_list = ['footwear_list','electronics_list','clothing_list']
    new_itm_list = {}
    print('************Login Page*************')

    guest = input('Please Enter A For Admin And U To Login As User?: ')

    if guest=='U':
        print('Login Success....')
        print('Please choose from below categories:')

        while exit_condition!='Y':

            print('1: Footwear          2: Electronics          3: Clothing          4: Check Cart          5: Payment          6: Logout')
            cat = input('Please choose from below categories:')

            if cat=='1':
                print('Category: Footwear')
                for val in footwear_list:
                    print(val+":" + footwear_list[val])

                foot_item = input('Please select Item to add in cart:')
                user_cart.append(footwear_list[foot_item])
                print(footwear_list[foot_item] +' Added into cart.')

            if cat == '2':
                print('Category: Electronics')
                for val in electronics_list:
                    print(val+":" + electronics_list[val])

                elec_item = input('Please select Item to add in cart:')
                user_cart.append(electronics_list[elec_item])
                print(electronics_list[elec_item] +' Added into cart.')

            if cat == '3':
                print('Category: Clothing')
                for val in clothing_list:
                    print(val+":" +  [val])

                cloth_item = input('Please select Item to add in cart:')
                user_cart.append(clothing_list[cloth_item])
                print(clothing_list[cloth_item] + ' Added into cart.')

            if cat == '4':
                print(user_cart)

            if cat == '5':
                print('Items Present In Cart: ')
                for x in range(0, len(user_cart)):
                    print(x+1 , ":"+user_cart[int(x)])

                cart_update = input("Want to modify Cart Y/N :")
                if cart_update=='Y':
                    while len(user_cart) > 0:
                        dlt_itm = input("Please select item to remove from above list or press Y for payment:")
                        if dlt_itm=='Y':
                            break
                        else:
                            print(user_cart)
                            print(user_cart[int(dlt_itm)-1] + " Item Removed From Cart")
                            if len(user_cart)-1>0:
                                user_cart.remove(user_cart[int(dlt_itm)-1])
                                print(user_cart)

                else:
                    print('1: UPI          2: Debit Card         3: Credit Card')
                    payment = input("Please Select Payment Type:")
                    if payment=='1' or payment =='2' or payment=='3':
                        print("Payment Successful.. Thank you...")
                        exit_condition = 'Y'

            if cat == '6':
                exit_condition = 'Y'
                break

        # guest = input('Please Enter A For Admin And U To Login As User?: ')

    else:
        username = input('Enter UserName: ')
        password = input('Enter Password: ')
        if username== 'admin' and password== 'root' :
            print('Login Success....')

            print('Available Categories: ')
            for val in category_list:
                print(val)

            print()
            print()
            print()

            print('Items Available in Footwear Category: ')
            for val in footwear_list:
                print(val + ":" + footwear_list[val])

            print('Items Available in Electronics Category: ')
            for val in electronics_list:
                print(val + ":" + electronics_list[val])

            print('Items Available in Clothing Category: ')
            for val in clothing_list:
                print(val + ":" + clothing_list[val])

            print("1: Add New Category")

            operation = input("Please select Operation you want to perform: ")

            if operation == '1':
                new_cat_name = input("Please Enter New Category Name: ")
                category_list.append(new_cat_name)
                i = 0
                add_itm = 'Y'
                while add_itm=='Y':
                    add_itm = input("Wants to add Items Y/N: ")
                    if add_itm=='Y':
                        new_cat_itm_name = input("Please Enter Item to add in new Category: ")
                        new_itm_list[i] = new_cat_itm_name
                    i+=1

                print("New Category with Item Added Successfully...")
        else:
            print('Wrong Credentials....')


get_input()


