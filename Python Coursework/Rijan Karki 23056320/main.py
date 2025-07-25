import read
import write
import operation

def get_customer_details():
    """
    Asks the user for their details and returns them.
    Handles invalid contact number input with retry.
    """
    while True:
        try:
            name = input("Enter your name: ")
            address = input("Enter your address: ")
            contact_no = int(input("Enter your contact number: "))
            return name, address, contact_no
        except:
            print("Invalid contact number. Please enter a numeric value.")

def display_furniture_details(furniture_details):
    """
    Display the details of furniture in a formatted table.
    """
    print("-" * 80)
    print("ID    Manufacturer               Product            Quantity   Price")
    print("-" * 80)
    for i in range(len(furniture_details)):
        id_field = furniture_details[i][0] + " " * (5 - len(furniture_details[i][0]))
        manufacturer_field = furniture_details[i][1] + " " * (30 - len(furniture_details[i][1]))
        product_field = furniture_details[i][2] + " " * (20 - len(furniture_details[i][2]))
        quantity_field = furniture_details[i][3] + " " * (10 - len(furniture_details[i][3]))
        price_field = furniture_details[i][4].replace('$', '') + " " * (10 - len(furniture_details[i][4].replace('$', '')))

        print(id_field + manufacturer_field + product_field + quantity_field + "$" + price_field)
        print("-" * 80)

def main():
    """
    Main function to manage the furniture store operations.
    Provides a menu to sell, buy furniture, or exit the program.
    """
    furniture_details = read.listt()

    while True:
        print("\n                       Welcome to the BRJ Furniture                                        ")
        print("1. Sell Furniture")
        print("2. Buy Furniture")
        print("3. Exit")

        try:
            selection = int(input("Enter the number of your choice: "))

            if selection == 1:
                display_furniture_details(furniture_details)
                furniture_id = input("\nEnter the ID you want to sell: ")
                quantity = int(input("Enter the quantity: "))

                if operation.decrease_quantity(furniture_details, furniture_id, quantity):
                    name, address, contact_no = get_customer_details()
                    invoice_details = {
                        'customer_name': name,
                        'customer_address': address,
                        'customer_contact': contact_no,
                        'items': [],
                        'shipping_cost': 50  # Example shipping cost
                    }
                    for item in furniture_details:
                        if item[0] == furniture_id:
                            invoice_details['items'].append({
                                'id': item[0],
                                'manufacturer': item[1],
                                'product': item[2],
                                'quantity': quantity,
                                'price': float(item[4].replace('$', ''))
                            })
                    write.write_invoice(invoice_details)
                    write.write_furniture_details(furniture_details)
                    print("Product has been sold.")

            elif selection == 2:
                display_furniture_details(furniture_details)
                furniture_id = input("\nEnter the ID of the furniture you want to buy: ")
                quantity = int(input("Enter the quantity: "))

                if operation.increase_quantity(furniture_details, furniture_id, quantity):
                    print("Furniture returned successfully.")
                    write.write_furniture_details(furniture_details)

            elif selection == 3:
                print("Thank you for visiting BRJ Furniture. Have a good day !!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 3.")

        except:
            print("An error occurred. Please enter a numeric value.")

if __name__ == "__main__":
    main()




