# Shopping Cart System

product_list = []
cart_list = []
user_list = ["Hema", "Rahul", "Priya"]
order_list = []

while True:

    print("\n====== SHOPPING CART SYSTEM ======")
    print("1. Admin")
    print("2. User")
    print("3. Exit")

    role = int(input("Enter your choice: "))

    # ---------------- ADMIN ----------------
    if role == 1:

        while True:

            print("\n------ ADMIN MENU ------")
            print("1. Add Product")
            print("2. Update Product")
            print("3. Remove Product")
            print("4. View Products")
            print("5. View Users")
            print("6. Back")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                name = input("Enter Product Name: ")
                price = float(input("Enter Product Price: "))

                product = [name, price]
                product_list.append(product)
                print("Product Added Successfully!")

            elif choice == 2:

                if len(product_list) == 0:
                    print("No Products Available")
                else:
                    print("\nProducts")
                    for i in range(len(product_list)):
                        print(i + 1, product_list[i])

                    index = int(input("Enter Product Number to Update: ")) - 1

                    if index >= 0 and index < len(product_list):
                        new_name = input("Enter New Product Name: ")
                        new_price = float(input("Enter New Price: "))

                        product_list[index][0] = new_name
                        product_list[index][1] = new_price

                        print("Product Updated Successfully")
                    else:
                        print("Invalid Product")

            elif choice == 3:

                if len(product_list) == 0:
                    print("No Products Available")
                else:
                    print("\nProducts")
                    for i in range(len(product_list)):
                        print(i + 1, product_list[i])

                    index = int(input("Enter Product Number to Remove: ")) - 1

                    if index >= 0 and index < len(product_list):
                        product_list.pop(index)
                        print("Product Removed")
                    else:
                        print("Invalid Product")

            elif choice == 4:

                if len(product_list) == 0:
                    print("No Products Available")
                else:
                    print("\nAvailable Products")
                    for i in range(len(product_list)):
                        print(i + 1, product_list[i])

            elif choice == 5:

                print("\nRegistered Users")
                for user in user_list:
                    print(user)

            elif choice == 6:
                break

            else:
                print("Invalid Choice")

    # ---------------- USER ----------------
    elif role == 2:

        username = input("Enter Your Name: ")
        if username not in user_list:
            user_list.append(username)

        while True:

            print("\n------ USER MENU ------")
            print("1. View Products")
            print("2. Add to Cart")
            print("3. Remove from Cart")
            print("4. View Cart")
            print("5. Checkout")
            print("6. Back")

            choice = int(input("Enter your choice: "))

            if choice == 1:

                if len(product_list) == 0:
                    print("No Products Available")
                else:
                    for i in range(len(product_list)):
                        print(i + 1, product_list[i])

            elif choice == 2:

                if len(product_list) == 0:
                    print("No Products Available")
                else:
                    for i in range(len(product_list)):
                        print(i + 1, product_list[i])

                    index = int(input("Enter Product Number: ")) - 1

                    if index >= 0 and index < len(product_list):
                        cart_list.append(product_list[index])
                        print("Product Added to Cart")
                    else:
                        print("Invalid Product")

            elif choice == 3:

                if len(cart_list) == 0:
                    print("Cart is Empty")
                else:
                    for i in range(len(cart_list)):
                        print(i + 1, cart_list[i])

                    index = int(input("Enter Item Number to Remove: ")) - 1

                    if index >= 0 and index < len(cart_list):
                        cart_list.pop(index)
                        print("Item Removed")
                    else:
                        print("Invalid Item")

            elif choice == 4:

                if len(cart_list) == 0:
                    print("Cart is Empty")
                else:
                    print("\nYour Cart")
                    total = 0

                    for item in cart_list:
                        print(item)
                        total = total + item[1]

                    print("Total =", total)

            elif choice == 5:

                if len(cart_list) == 0:
                    print("Cart is Empty")
                else:
                    total = 0

                    print("\n------ BILL ------") 
                    for item in cart_list:
                        print(item)
                        total = total + item[1]

                    print("Total Amount =", total)

                    order_list.append(cart_list.copy())
                    cart_list.clear()

                    print("Order Placed Successfully!")

            elif choice == 6:
                break

            else:
                print("Invalid Choice")

    elif role == 3:
        print("Thank You for Using Shopping Cart System")
        break

    else:
        print("Invalid Choice")
