# Write a class that meets these requirements.
#
# Name:       Receipt
#
# Required state:
#    * tax rate, the percentage tax that should be applied to the total
#
# Behavior:
#    * add_item(item)   # Add a ReceiptItem to the Receipt
#    * get_subtotal()   # Returns the total of all of the receipt items
#    * get_total()      # Multiplies the subtotal by the 1 + tax rate
#
# Example:
#    item = Receipt(.1)
#    item.add_item(ReceiptItem(4, 2.50))
#    item.add_item(ReceiptItem(2, 5.00))
#
#    print(item.get_subtotal())     # Prints 20
#    print(item.get_total())        # Prints 22


# class Receipt
    # method initializer with tax rate
        # self.tax_rate = tax_rate
        # self.items = new empty list

    # method add_item(self, item)
        # append item to self.items list

    # method get_subtotal(self)
        # sum = 0
        # for each item in self.items
            # increase sum by item.get_total()
        # return sum

    # method get_total(self)
        # return self.get_subtotal() * (1 + self.tax_rate)

class Receipt:
    def __init__(self, tax_rate):
        self.tax_rate = tax_rate
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_subtotal(self):
        sum = 0
        for item in self.items:
            sum += item.get_total()
        return sum

    def get_total(self):
        return self.get_subtotal() * (1 + self.tax_rate)
