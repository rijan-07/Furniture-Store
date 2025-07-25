# write.py
import datetime

def write_furniture_details(furniture_details):
    """
    Write the updated furniture details to the file.
    """
    file = open("furnituredetails.txt", "w")
    for furniture in furniture_details:
        file.write(furniture[0] + ", " +
                   furniture[1] + ", " +
                   furniture[2] + ", " +
                   furniture[3] + ", " +
                   "$" + furniture[4] + "\n")
    file.close()

def write_invoice(invoice_details):
    """
    Write the invoice details to a new file with a unique invoice ID.
    """
    invoice_id = generate_invoice_id()  # Function to generate a unique invoice ID
    file = open(invoice_id + ".txt", "w")
    file.write("Invoice Details\n")
    file.write("Customer Name: " + invoice_details['customer_name'] + "\n")
    file.write("Customer Address: " + invoice_details['customer_address'] + "\n")
    file.write("Customer Contact Number: " + str(invoice_details['customer_contact']) + "\n")
    file.write("\nFurniture Purchased:\n")
    
    total_amount = 0
    for item in invoice_details['items']:
        file.write("ID: " + item['id'] + ", " +
                   "Manufacturer: " + item['manufacturer'] + ", " +
                   "Product: " + item['product'] + ", " +
                   "Quantity: " + str(item['quantity']) + ", " +
                   "Price: $" + str(item['price']) + "\n")
        total_amount += item['price'] * item['quantity']
    
    vat_amount = total_amount * 0.13
    shipping_cost = invoice_details['shipping_cost']
    total_amount_with_vat_shipping = total_amount + vat_amount + shipping_cost

    file.write("\nSubtotal: $" + str(total_amount) + "\n")
    file.write("VAT (13%): $" + str(vat_amount) + "\n")
    file.write("Shipping Cost: $" + str(shipping_cost) + "\n")
    file.write("Total Amount: $" + str(total_amount_with_vat_shipping) + "\n")
    file.close()

def generate_invoice_id():
    """
    Generate a unique invoice ID.
    """
    now = datetime.datetime.now()
    return "INVOICE" + now.strftime("%Y_%m_%d_%H_%M_%S")


