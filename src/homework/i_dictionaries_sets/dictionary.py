def add_inventory(inventory, item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
def remove_inventory_widget(inventory, widget_name, quantity=None):
 
    if widget_name not in inventory:
        return "Item not found"

    if quantity is None:
        del inventory[widget_name]
        return "Record deleted"

    if inventory[widget_name] < quantity:
        return f"Error: Not enough {widget_name} to remove."

    inventory[widget_name] -= quantity
    return inventory[widget_name]


    