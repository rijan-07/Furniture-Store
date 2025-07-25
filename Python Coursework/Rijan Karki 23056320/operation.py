# operation.py
def decrease_quantity(furniture_list, furniture_id, quantity):
    """
    Decrease the quantity of the specified furniture in the inventory.
    """
    for i in range(len(furniture_list)):
        if furniture_list[i][0] == furniture_id:
            if int(furniture_list[i][3]) >= quantity:
                furniture_list[i][3] = str(int(furniture_list[i][3]) - quantity)
                return True
            else:
                print("Not enough quantity available.")
                return False
    print("Furniture ID not found.")
    return False

def increase_quantity(furniture_list, furniture_id, quantity):
    """
    Increase the quantity of the specified furniture in the inventory.
    """
    for i in range(len(furniture_list)):
        if furniture_list[i][0] == furniture_id:
            furniture_list[i][3] = str(int(furniture_list[i][3]) + quantity)
            return True
    print("Furniture ID not found.")
    return False

def check_availability(furniture_list, furniture_id):
    """
    Check the availability of furniture based on the ID.
    """
    for i in range(len(furniture_list)):
        if furniture_list[i][0] == furniture_id:
            if int(furniture_list[i][3]) > 0:
                return "Available"
            else:
                return "Not Available"
    print("Furniture ID not found.")
    return "Not Available"




